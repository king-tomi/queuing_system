import React from 'react';
import { Routes, Route } from 'react-router-dom';
import HomePage from './components/Home';
import LoginPage from './components/Login';
// Import other components/routes as needed

const AppRouter = () => {
  return (
    <Routes>
      <Route exact path="/" element={<HomePage />} />
      <Route path="/login" element={<LoginPage />} />
      {/* Add other routes */}
    </Routes>
  );
};

export default AppRouter;