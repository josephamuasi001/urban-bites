function StatCard({ number, text }) {
  return (
    <div className="stat-card">
      <h3>{number}</h3>
      <p>{text}</p>
    </div>
  );
}

export default StatCard;