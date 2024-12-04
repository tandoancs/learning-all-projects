import './App.css';
import logo from './logo.svg';

import { signInWithGooglePopup } from "./config"; // Assuming the correct path to your configuration file

function App() {
  const logGoogleUser = async () => {
    const response = await signInWithGooglePopup();
    console.log(response);
  }
  return (
    <div>
      <header className="App-header">
      
        <img src={logo} className="App-logo" alt="logo" />
      
        <button className="App-button" onClick={logGoogleUser}>Sign In With Google</button>
      </header>
      
    </div>
  )
}

export default App;
