import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "MOCK_API_KEY",
  authDomain: "startupos-mock.firebaseapp.com",
  projectId: "startupos-mock",
  storageBucket: "startupos-mock.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdef"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
