import { createUserWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase";
import { useState } from "react";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const signup = async () => {
    await createUserWithEmailAndPassword(auth, email, password);
    window.location.href = "/login";
  };

  return (
    <div>
      <h2>Signup</h2>
      <input onChange={(e)=>setEmail(e.target.value)} placeholder="Email"/>
      <input type="password" onChange={(e)=>setPassword(e.target.value)} placeholder="Password"/>
      <button onClick={signup}>Signup</button>
    </div>
  );
}
