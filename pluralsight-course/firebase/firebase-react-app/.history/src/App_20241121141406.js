import React, { useEffect, useState } from "react";
import './App.css';


import { onAuthStateChanged } from "firebase/auth";
import { auth, signIn } from "./configuration"; // Assuming the correct path to your configuration file



function App() {

  const [data, setData] = useState([]);

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
