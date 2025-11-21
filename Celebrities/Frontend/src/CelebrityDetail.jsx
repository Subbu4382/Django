import { useParams, Link } from "react-router-dom";
import { useEffect, useState } from "react";

function CelebrityDetail() {
  const { id } = useParams();
  const [celebrity, setCelebrity] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/data/${id}`)
      .then(res => res.json())
      .then(data => setCelebrity(data));
  }, [id]);

  if (!celebrity) return <h2 style={{ textAlign: "center" }}>Loading...</h2>;

  return (
    <div>
      <div className="detail-container">
        <img 
          src={celebrity.profile_pic}
          className="detail-img"
          alt={celebrity.name}
        />

        <div className="detail-info">
          <h1>{celebrity.name}</h1>
          <p><b>Age:</b> {celebrity.age}</p>
          <p><b>Gender:</b> {celebrity.gender}</p>
          <p><b>Profession:</b> {celebrity.profession}</p>
          <p><b>Followers:</b> {celebrity.followers}</p>
          <p><b>Nationality:</b> {celebrity.nationality}</p>
          <p><b>DOB:</b> {celebrity.DOB}</p>
        </div>
      </div>

      <div style={{ textAlign: "center" }}>
        <Link to="/" className="back-btn">← Back to List</Link>
      </div>
    </div>
  );
}

export default CelebrityDetail;
