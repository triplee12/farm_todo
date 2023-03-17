import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className='App card shadow p-3 rounded list-group-item justify-content-center align-items-center mx-auto' style={{ "width": "400px", "backgroundColor": "white", "marginTop": "15px" }}>
      <h1 className='card text-white bg-primary mb-1' styleName="max-width: 20rem;">Task Manager</h1>
      <h5 className='card text-white bg-primary mb-3'>Start New Fastapi Project</h5>
      <div className='card-body'>
        <h6 className='card text-white bg-dark mb-3'>Add Task</h6>
        <span className='card-text'>
          <input className='mb-2 form-control titleIn' placeholder='Enter title' />
          <input className='mb-2 form-control descIn' placeholder='Enter description' />
          <button className='btn btn-outline-primary mx-2' style={{ "borderRadius": "50px", "fontWeight": "bold"}}>Add Task</button>
        </span>
        <h6 className='card text-white bg-dark mb-3 mt-3'>Your Tasks</h6>
        <div>External components</div>
      </div>
      <h6 className='card text-dard bg-warning py-1 mb-0 mt-2' style={{"height": "30px", "textAlign": "center"}}>
        Copyright &copy; 2023 all right reserved.
      </h6>
    </div>
  );
}

export default App;
