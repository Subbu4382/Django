import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function CelebrityList() {
  const [celebrities, setCelebrities] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/Alldata/")
      .then(res => res.json())
      .then(data => setCelebrities(data));
  }, []);

  return (
    <div className="page-container">
      <h1 style={{ marginBottom: "25px", textAlign: "center" }}>
        Celebrity Gallery
      </h1>

      <div className="celebrity-grid">
        {celebrities.map(c => (
          <Link 
            key={c.id} 
            to={`/celebrity/${c.id}`} 
            style={{ textDecoration: "none" }}
          >
            <div className="celebrity-card">
              <img 
                src={c.profile_pic} 
                alt={c.name}
                className="celebrity-img"
              />
              <h3>{c.name}</h3>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default CelebrityList;
