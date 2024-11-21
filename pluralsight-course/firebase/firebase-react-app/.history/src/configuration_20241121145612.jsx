// Import the necessary Firebase modules
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your Firebase config here
const firebaseConfig = {
    apiKey: "AIzaSyDf1ATehZCbdwDnrAEHtUJorjzyMrkmMWM",
    authDomain: "msea-project.firebaseapp.com",
    projectId: "msea-project",
    storageBucket: "msea-project.firebasestorage.app",
    messagingSenderId: "842910639353",
    appId: "1:842910639353:web:67111ca2b2247579402e28"
  };

// Initialize Firebase
const firebase = initializeApp(firebaseConfig);

// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(firebase);

export { auth, firebase, provider };
// Now you can use Firebase services in your React app!