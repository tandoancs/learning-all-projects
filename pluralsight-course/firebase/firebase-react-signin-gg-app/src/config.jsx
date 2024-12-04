// Import the necessary Firebase modules
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";

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

// Initialize Firebase Auth provider
const provider = new GoogleAuthProvider();

// whenever a user interacts with the provider, we force them to select an account
provider.setCustomParameters({
  prompt: "select_account "
});

// Sign In With Google by Popup
const signInWithGooglePopup = () => signInWithPopup(auth, provider);

export { auth, firebase, signInWithGooglePopup };

// Now you can use Firebase services in your React app!