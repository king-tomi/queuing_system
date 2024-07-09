import React, { useState } from 'react';
import api from '../api'; // Adjusted path to api.js
import '../styles/Login.css'; // Adjusted path to Login.css

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('customer'); // Default role
    const [error, setError] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post(`/${role}s/`, { email, password });
            const token = response.data.token;
            localStorage.setItem('token', token);
            setError('');
            // Redirect to the appropriate page based on role
            if (role === 'customer') {
                window.location.href = '/customer-dashboard';
            } else if (role === 'bankstaff') {
                window.location.href = '/staff-dashboard';
            }
        } catch (err) {
            setError('Invalid email or password');
        }
    };

    return (
        <div className="login-container">
            <form onSubmit={handleLogin}>
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
                <select value={role} onChange={(e) => setRole(e.target.value)}>
                    <option value="customer">Customer</option>
                    <option value="bankstaff">Bank Staff</option>
                </select>
                <button type="submit">Login</button>
                {error && <div className="error">{error}</div>}
            </form>
        </div>
    );
};

export default Login;