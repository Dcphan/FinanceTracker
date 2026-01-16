import { useState } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import {useAuth} from "./hook/useAuth"
import { LoginPage } from './pages/LoginPage'
import { BudgetApp } from './pages/BudgetApp'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  const { login } = useAuth();
  const [showSignUp, setShowSignUp] = useState(false);
  const authorized = false;

  return (
      <BrowserRouter>
        <Routes>
            <Route path="/login" element={<LoginPage onLogin={login} onSwitchToSignUp={() => setShowSignUp(true)}/>}/>
            <Route path="/dashboard" element={<BudgetApp userName={"No Name"}/>}/>
        </Routes>               
      </BrowserRouter>
    );
}

export default App
