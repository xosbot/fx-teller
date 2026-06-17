import Constants from 'expo-constants';

const extra = (Constants.expoConfig?.extra ?? {}) as { apiUrl?: string };
export const API_URL = extra.apiUrl || 'http://localhost:3000/api';
export const APP_NAME = 'FX-Teller';
export const APP_SCHEME = 'fxteller';
