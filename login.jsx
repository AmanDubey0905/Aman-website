import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase";
import { useState } from "react";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    await signInWithEmailAndPassword(auth, email, password);
    window.location.href = "/dashboard";
  };

  return (
    <div>
      <h2>Login</h2>
      <input onChange={(e)=>setEmail(e.target.value)} placeholder="Email"/>
      <input type="password" onChange={(e)=>setPassword(e.target.value)} placeholder="Password"/>
      <button onClick={login}>Login</button>
    </div>
  );
}
