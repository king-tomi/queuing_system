// src/store/auth/authActions.js
import axios from '../../axiosConfig';
import jwtDecode from 'jwt-decode';

// Define your action types
const LOGIN_SUCCESS = 'LOGIN_SUCCESS';
const LOGOUT = 'LOGOUT';

// Action creators
export const login = (credentials) => async (dispatch) => {
    try {
        const response = await axios.post('/auth/jwt/create/', credentials);
        const token = response.data.access;
        const user = jwtDecode(token);
        dispatch({ type: LOGIN_SUCCESS, payload: { token, user } });
        localStorage.setItem('token', token);
    } catch (error) {
        console.error(error);
    }
};

export const logout = () => {
    localStorage.removeItem('token');
    return { type: LOGOUT };
};

// src/store/auth/authReducer.js
const initialState = {
    token: localStorage.getItem('token') || null,
    user: localStorage.getItem('token') ? jwtDecode(localStorage.getItem('token')) : null,
};

const authReducer = (state = initialState, action) => {
    switch (action.type) {
        case 'LOGIN_SUCCESS':
            return {
                ...state,
                token: action.payload.token,
                user: action.payload.user,
            };
        case 'LOGOUT':
            return {
                ...state,
                token: null,
                user: null,
            };
        default:
            return state;
    }
};

export default authReducer;