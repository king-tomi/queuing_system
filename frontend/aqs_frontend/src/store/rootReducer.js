// src/store/rootReducer.js
import { combineReducers } from 'redux';
import authReducer from './auth/authReducer';

const rootReducer = combineReducers({
    auth: authReducer,
    // Add other reducers here
});

export default rootReducer;