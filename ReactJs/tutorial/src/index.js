import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './ex1-helloworld';
import Ex2 from './ex2-components-props';
import Ex3 from './ex3-ternary-lists-import';
import Ex4 from './ex4-states';
import Ex5 from './ex5-CRUD';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <Ex2 />
    <Ex3 />
    <Ex4 />
    <Ex5 />
  </React.StrictMode>
);
