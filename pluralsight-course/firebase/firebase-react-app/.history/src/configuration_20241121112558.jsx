// Import the necessary Firebase modules
import { initializeApp } from "firebase/app";

// Your Firebase config here
const firebaseConfig = {
    apiKey: "AIzaSyDf1ATehZCbdwDnrAEHtUJorjzyMrkmMWM",
    authDomain: "msea-project.firebaseapp.com",
    projectId: "msea-project",
    storageBucket: "msea-project.firebasestorage.app",
    messagingSenderId: "842910639353",
    appId: "1:842910639353:web:76f49206bf66de07402e28"
};

// Initialize Firebase
const firebase = initializeApp(firebaseConfig);

// Initialize Firebase Authentication and get a reference to the service
// const auth = getAuth(app);

export default firebase;
// Now you can use Firebase services in your React app!