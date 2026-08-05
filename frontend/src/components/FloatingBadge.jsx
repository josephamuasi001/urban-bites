function FloatingBadge({ icon, title, value, className = "" }) {
  return (
    <div className={`floating-badge ${className}`}>
      <div className="floating-icon">
        {icon}
      </div>

      <div className="floating-content">
        <small>{title}</small>
        <strong>{value}</strong>
      </div>
    </div>
  );
}

export default FloatingBadge;