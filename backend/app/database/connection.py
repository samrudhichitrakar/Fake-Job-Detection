"""
Database connection and operations module
Handles MySQL database connections and CRUD operations
"""
import mysql.connector
from mysql.connector import Error
from typing import Optional, Dict, Any
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import Config

class Database:
    """Database connection manager for MySQL"""
    
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Establish connection to MySQL database"""
        try:
            self.connection = mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
                port=Config.DB_PORT
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("Successfully connected to MySQL database")
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            if self.cursor:
                self.cursor.close()
            self.connection.close()
            print("MySQL connection closed")
    
    def save_prediction(self, input_type: str, job_text: str, 
                       image_path: Optional[str], prediction_label: str,
                       confidence_score: float, extracted_text: Optional[str],
                       reason: str) -> int:
        """Save prediction result to database"""
        try:
            query = """
                INSERT INTO predictions 
                (input_type, job_text, image_path, prediction_label, 
                 confidence_score, extracted_text, reason)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (input_type, job_text, image_path, prediction_label,
                     confidence_score, extracted_text, reason)
            
            self.cursor.execute(query, values)
            self.connection.commit()
            return self.cursor.lastrowid
        except Error as e:
            print(f"Error saving prediction: {e}")
            return -1
    
    def get_predictions(self, limit: int = 100):
        """Retrieve recent predictions from database"""
        try:
            query = """
                SELECT * FROM predictions 
                ORDER BY created_at DESC 
                LIMIT %s
            """
            self.cursor.execute(query, (limit,))
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error fetching predictions: {e}")
            return []
    
    def save_model_metrics(self, model_name: str, accuracy: float,
                          precision: float, recall: float, f1: float):
        """Save model performance metrics"""
        try:
            query = """
                INSERT INTO model_metrics 
                (model_name, accuracy, precision_score, recall_score, f1_score)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (model_name, accuracy, precision, recall, f1)
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error saving metrics: {e}")
            return False
