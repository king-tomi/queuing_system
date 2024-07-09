import axios from 'axios';

// Create an Axios instance
const api = axios.create({
    baseURL: process.env.REACT_APP_API_URL, // Replace with your backend API base URL
});

// Add a request interceptor to include the token
api.interceptors.request.use(
    (config) => {
        const token = process.env.REACT_APP_TOKEN; // Access token from .env file
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;