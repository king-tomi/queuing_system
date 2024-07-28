import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import Login from './Login';
import Teller from './Teller'; // Import Teller component
import CSO from './cs_officer'; // Import CSO component

const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/login" element={<Login />} />
      <Route path="/home" element={<Home />} />
      <Route path="/teller" element={<Teller />} />
      <Route path="/cso" element={<CSO />} />
      {/* Add other routes as needed */}
    </Routes>
  );
};

export default AppRouter;