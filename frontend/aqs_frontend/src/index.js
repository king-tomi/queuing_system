// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';
import store from './store/store';
import AppRouter from './Router';
import 'antd/dist/antd.css'; // Ant Design styles

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <AppRouter />
        </Router>
    </Provider>,
    document.getElementById('root')
);