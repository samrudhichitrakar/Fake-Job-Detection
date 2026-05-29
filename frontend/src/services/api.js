/**
 * API Service
 * Handles all API calls to the FastAPI backend
 */
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Predict if job text is fake or genuine
 * @param {string} text - Job posting text
 * @returns {Promise} Prediction result
 */
export const predictText = async (text) => {
  try {
    const response = await api.post('/predict-text', { text });
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Error predicting text';
  }
};

/**
 * Predict from uploaded image file
 * @param {File} file - Image file
 * @returns {Promise} Prediction result
 */
export const predictImage = async (file) => {
  try {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await axios.post(`${API_BASE_URL}/predict-image`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Error predicting image';
  }
};

/**
 * Predict from image URL
 * @param {string} imageUrl - URL of the image
 * @returns {Promise} Prediction result
 */
export const predictImageURL = async (imageUrl) => {
  try {
    const response = await api.post('/predict-image-url', { image_url: imageUrl });
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Error predicting image URL';
  }
};

/**
 * Get model information
 * @returns {Promise} Model info
 */
export const getModelInfo = async () => {
  try {
    const response = await api.get('/model-info');
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Error fetching model info';
  }
};

/**
 * Health check
 * @returns {Promise} Health status
 */
export const healthCheck = async () => {
  try {
    const response = await api.get('/health');
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Error checking health';
  }
};

export default api;
