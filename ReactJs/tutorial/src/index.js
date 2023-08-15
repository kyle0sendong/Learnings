import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './ex1-helloworld';
import Ex2 from './ex2-components-props';
import Ex3 from './ex3-ternary-lists-import';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <Ex2 />
    <Ex3 />
  </React.StrictMode>
);
