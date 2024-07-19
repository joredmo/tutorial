import axios from 'axios';
import { ACCESS_TOKEN } from './constants';

const apiUrl = "/choreo-apis/turorial/backend/v1"

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl,
  });

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN); // get token from local storage
        if (token) { // if token exists
            config.headers.Authorization = `Bearer ${token}`; // add token to header
        }
        return config; // return config
    },
    (error) => { // handle error
        return Promise.reject(error); // reject promise with error
    }
);

export default api;