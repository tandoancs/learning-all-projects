import React, { useEffect } from "react";
import './App.css';

import { onAuthStateChanged, signInAnonymously } from "firebase/auth";
import { auth } from "./config"; // Assuming the correct path to your configuration file



function App() {

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
