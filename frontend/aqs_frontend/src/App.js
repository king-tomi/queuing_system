import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Teller from './Teller';
import CSO from './cs_officer'; // Ensure correct casing here

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} /> {/* Default route */}
                <Route path="/login" element={<Login />} />
                <Route path="/teller" element={<Teller />} />
                <Route path="/cso" element={<CSO />} />
            </Routes>
        </Router>
    );
};

export default App;