// src/store/rootReducer.js
import { combineReducers } from 'redux';
import authReducer from './auth/authActions';

const rootReducer = combineReducers({
    auth: authReducer,
    // Add other reducers here
});

export default rootReducer;