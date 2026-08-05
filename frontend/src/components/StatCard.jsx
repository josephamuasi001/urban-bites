function StatCard({ number, label }) {
  return (
    <div className="stat-card">
      <h2>{number}</h2>
      <span>{label}</span>
    </div>
  );
}

export default StatCard;