import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from './api'; // Adjust the import path as necessary

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async () => {
        // Check if email and password are provided.
        if (email && password) {
            try {
                // Make the API request.
                const response = await api.post('/login', { email, password });

                // Check if the response is successful.
                if (response.status === 200) {
                    const data = response.data;

                    // Assuming the API returns a user role in the response data.
                    const userRole = data.position;

                    // Navigate based on user role.
                    if (userRole === 'teller') {
                        navigate('/teller');
                    } else if (userRole === 'cso') {
                        navigate('/cso');
                    } else {
                        // Handle unknown roles or additional logic here.
                        console.error('Unknown user role:', userRole);
                    }
                } else {
                    // Handle unsuccessful response (e.g., invalid credentials).
                    console.error('Login failed:', response.statusText);
                    alert('Invalid email or password. Please try again.');
                }
            } catch (error) {
                // Handle network or other errors.
                console.error('Error during login:', error);
                alert('An error occurred during login. Please try again later.');
            }
        } else {
            // Handle missing email or password.
            alert('Please enter both email and password.');
        }
    };

    return (
        <div>
            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
};

export default Login;