"""
Model Training Script for Fake Job Detection
Trains LSTM/BiLSTM model on Kaggle Fake Job Postings dataset
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Bidirectional, Dense, Dropout, SpatialDropout1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Set memory growth for GPU (if available)
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    try:
        for device in physical_devices:
            tf.config.experimental.set_memory_growth(device, True)
    except:
        pass
import joblib
import os
from app.services.text_preprocessor import TextPreprocessor
from config import Config

def load_dataset(file_path='fake_jobs.csv'):
    """Load and prepare the Kaggle Fake Job Postings dataset"""
    print("Loading dataset...")
    
    # If dataset doesn't exist, create a sample dataset
    if not os.path.exists(file_path):
        print("Dataset not found. Creating sample dataset...")
        # Sample data for demonstration
        data = {
            'title': ['Software Engineer', 'Data Scientist', 'Work from Home - Easy Money', 
                     'Marketing Manager', 'Get Rich Quick - No Experience'],
            'company_profile': ['Established tech company', 'Fortune 500 company', 
                               'Unknown company', 'Reputable firm', 'Suspicious company'],
            'description': ['Develop software applications', 'Analyze data and build models',
                           'Make $5000 per week from home with no effort',
                           'Lead marketing campaigns', 'Earn money fast with zero investment'],
            'requirements': ['BS in CS, 3 years exp', 'MS in Statistics, Python skills',
                            'No experience needed', 'MBA, 5 years exp', 'Anyone can apply'],
            'fraudulent': [0, 0, 1, 0, 1]
        }
        df = pd.DataFrame(data)
    else:
        df = pd.read_csv(file_path)
    
    print(f"Dataset loaded: {len(df)} records")
    return df

def prepare_data(df):
    """Prepare and preprocess data for training"""
    print("Preparing data...")
    
    # Combine text fields
    df['text'] = (df['title'].fillna('') + ' ' + 
                  df['company_profile'].fillna('') + ' ' +
                  df['description'].fillna('') + ' ' +
                  df['requirements'].fillna(''))
    
    # Preprocess text
    preprocessor = TextPreprocessor()
    df['processed_text'] = df['text'].apply(preprocessor.preprocess)
    
    # Remove empty texts
    df = df[df['processed_text'].str.len() > 0]
    
    X = df['processed_text'].values
    y = df['fraudulent'].values
    
    print(f"Fake jobs: {sum(y)}, Genuine jobs: {len(y) - sum(y)}")
    
    return X, y

def create_model(max_features, max_length, embedding_dim=128):
    """
    Create BiLSTM model for fake job detection
    Architecture: Embedding -> BiLSTM -> Dense -> Output
    """
    model = Sequential([
        # Embedding layer
        Embedding(input_dim=max_features, output_dim=embedding_dim, input_length=max_length),
        SpatialDropout1D(0.2),
        
        # Bidirectional LSTM layers
        Bidirectional(LSTM(64, return_sequences=True, dropout=0.2, recurrent_dropout=0.2)),
        Bidirectional(LSTM(32, dropout=0.2, recurrent_dropout=0.2)),
        
        # Dense layers
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(32, activation='relu'),
        Dropout(0.3),
        
        # Output layer
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def train_model():
    """Main training function"""
    # Create directories
    os.makedirs('ml_models', exist_ok=True)
    
    # Load and prepare data
    df = load_dataset()
    X, y = prepare_data(df)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    
    # Tokenization
    print("Tokenizing text...")
    tokenizer = Tokenizer(num_words=Config.MAX_FEATURES, oov_token='<OOV>')
    tokenizer.fit_on_texts(X_train)
    
    X_train_seq = tokenizer.texts_to_sequences(X_train)
    X_test_seq = tokenizer.texts_to_sequences(X_test)
    
    # Padding
    X_train_pad = pad_sequences(X_train_seq, maxlen=Config.MAX_SEQUENCE_LENGTH, padding='post')
    X_test_pad = pad_sequences(X_test_seq, maxlen=Config.MAX_SEQUENCE_LENGTH, padding='post')
    
    # Create model
    print("Creating model...")
    model = create_model(Config.MAX_FEATURES, Config.MAX_SEQUENCE_LENGTH, Config.EMBEDDING_DIM)
    print(model.summary())
    
    # Callbacks
    early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    checkpoint = ModelCheckpoint(Config.MODEL_PATH, save_best_only=True, monitor='val_accuracy')
    
    # Train model
    print("Training model...")
    history = model.fit(
        X_train_pad, y_train,
        validation_data=(X_test_pad, y_test),
        epochs=10,
        batch_size=32,
        callbacks=[early_stop, checkpoint],
        verbose=1
    )
    
    # Evaluate model
    print("\nEvaluating model...")
    y_pred_prob = model.predict(X_test_pad)
    y_pred = (y_pred_prob > 0.5).astype(int).flatten()
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Genuine', 'Fake']))
    
    # Save tokenizer
    print("\nSaving tokenizer...")
    joblib.dump(tokenizer, Config.TOKENIZER_PATH)
    
    print(f"\nModel saved to {Config.MODEL_PATH}")
    print(f"Tokenizer saved to {Config.TOKENIZER_PATH}")
    print("\nTraining completed successfully!")
    
    return model, tokenizer, accuracy, precision, recall, f1

if __name__ == "__main__":
    train_model()
