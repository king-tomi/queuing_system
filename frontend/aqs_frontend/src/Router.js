// src/Router.js
import React from 'react';
import { Switch, Route } from 'react-router-dom';
import HomePage from './components/Home';
import LoginPage from './components/Login';
// Import other components/routes as needed

const AppRouter = () => (
    <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/login" component={LoginPage} />
        {/* Add other routes */}
    </Switch>
);

export default AppRouter;