import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './ex1-helloworld';
import Ex2 from './ex2-components-props';
import Ex3 from './ex3-ternary-lists-import';
import Ex4 from './ex4-states';
import Ex5 from './ex5-CRUD';
import Ex6 from './ex6-lifecycle';
import Ex7 from './ex7-api';
import Ex8 from './ex8-router-dom';
import Ex9 from './ex9';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <Ex2 />
    <Ex3 />
    <Ex4 />
    <Ex5 />
    <Ex6 />
    <Ex7 />
    <Ex8 />
    <Ex9 />
  </React.StrictMode>
);
