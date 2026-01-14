import { useState } from 'react'
import {useAuth} from "./hook/useAuth"
import { LoginPage } from './pages/LoginPage'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  const { login } = useAuth();
  const [showSignUp, setShowSignUp] = useState(false);

  return <LoginPage onLogin={login} onSwitchToSignUp={() => setShowSignUp(true)}/>;
}

export default App
