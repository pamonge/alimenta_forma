import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import About from './routes/About';
import Coorp from './routes/Coorp';
import Courses from './routes/Courses';
import Faqs from './routes/Faqs';
import Home from './routes/Home';
import Jobs from './routes/Jobs';
import Login from './routes/Login';
import Membership from './routes/Membership';
import Register from './routes/Register';
import Profile from './routes/Profile';
import Teacher from './routes/Teacher';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/login' element={<Login />} />
        <Route path='/register' element={<Register />} />
        <Route path='/about' element={<About />} />
        <Route path='/membership' element={<Membership />} />
        <Route path='/coorp' element={<Coorp />} />
        <Route path='/courses' element={<Courses />} />
        <Route path='/faqs' element={<Faqs />} />
        <Route path='/jobs' element={<Jobs />} />
        <Route path='/profile' element={<Profile />} />
        <Route path='/teacher' element={<Teacher />} />
      </Routes>
    </>
  )
}

export default App
