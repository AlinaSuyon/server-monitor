from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timedelta


DATABASE_URL = "sqlite:///./app/monitor.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class MetricRecord(Base):
    __tablename__ = "metrics_history"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cpu_percent = Column(Float)
    memory_percent = Column(Float)
    disk_percent = Column(Float)
    network_sent_mb = Column(Float)
    network_received_mb = Column(Float)


def init_db():
    Base.metadata.create_all(bind=engine)


def save_metrics(metrics: dict):
    db = SessionLocal()
    record = MetricRecord(
        cpu_percent=metrics["cpu"]["percent"],
        memory_percent=metrics["memory"]["percent"],
        disk_percent=metrics["disk"]["percent"],
        network_sent_mb=metrics["network"]["sent_mb"],
        network_received_mb=metrics["network"]["received_mb"],
    )
    db.add(record)
    db.commit()
    db.close()


def cleanup_old_records(days: int = 30):
    db = SessionLocal()
    cutoff = datetime.utcnow() - timedelta(days=days)
    db.query(MetricRecord).filter(MetricRecord.timestamp < cutoff).delete()
    db.commit()
    db.close()
