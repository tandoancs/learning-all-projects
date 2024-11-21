import React, { useEffect, useState } from "react";
import './App.css';


import { onAuthStateChanged, signInAnonymously } from "firebase/auth";
import { auth } from "./configuration"; // Assuming the correct path to your configuration file



function App() {

  const [data, setData] = useState([]);

  const signIn = () => {
    
    signInAnonymously(auth);

  };

  useEffect(() => {

    signIn();
    onAuthStateChanged(auth, (user) => {
      console.log(user);
    });
  }, []);

  return (
    <div>
      <h1>Sign In Anonymously</h1>
      
    </div>
  );
}

export default App;
