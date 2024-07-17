import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';
import store from './store/store';
import AppRouter from './Router';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import bootstrap

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <AppRouter />
        </Router>
    </Provider>,
    document.getElementById('root')
);