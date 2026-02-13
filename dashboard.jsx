import { useEffect, useState } from "react";
import { API_BASE_URL } from "../config";
import { auth } from "../firebase";

export default function Dashboard() {
  const [docs, setDocs] = useState([]);

  useEffect(() => {
    const user = auth.currentUser;
    fetch(`${API_BASE_URL}/documents?user_id=${user.uid}`)
      .then(res => res.json())
      .then(data => setDocs(data));
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      {docs.map(doc => (
        <div key={doc.id}>
          {doc.name} - {doc.status}
        </div>
      ))}
    </div>
  );
}
