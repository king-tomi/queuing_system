import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../Home.css';

const Home = () => {
  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate('/login');
  };

  return (
    <div className="home-container">
      <header className="home-header">
        <button className="login-button" onClick={handleLoginClick}>Login</button>
      </header>
      <div className="home-content">
        <h1>AUTOMATIC QUEUING SYSTEM FOR UBA, NIGERIA</h1>
        <p>Your efficient solution for managing queues and improving service delivery.</p>
      </div>
      <footer className="home-footer">
        <span>&copy; temmytee</span>
        <span>Powered by University of Ibadan</span>
      </footer>
    </div>
  );
};

export default Home;