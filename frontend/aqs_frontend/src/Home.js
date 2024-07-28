import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

const Home = () => {
  const navigate = useNavigate();

  const handleTellerClick = () => {
    navigate('/teller');
  };

  const handleCSOClick = () => {
    navigate('/cso');
  };

  return (
    <div className="home-container">
      <header className="home-header">
        <button className="logout-button" onClick={() => navigate('/login')}>Logout</button>
      </header>
      <div className="home-content">
        <h1>Welcome!</h1>
        <p>Select how you want us to serve you today from the services</p>
        <div className="service-options">
          <div className="service-option" onClick={handleTellerClick}>
            <img src="../public/teller.png" alt="Teller Transactions" />
            <button>View Teller Queue</button>
          </div>
          <div className="service-option" onClick={handleCSOClick}>
            <img src="../public/cso.png" alt="CSO Transactions" />
            <button>View CSO Queue</button>
          </div>
        </div>
      </div>
      <footer className="home-footer">
        <span>&copy; temmytee</span>
        <span>Powered by University of Ibadan</span>
      </footer>
    </div>
  );
};

export default Home;