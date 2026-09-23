from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    mood = Column(Integer, nullable=False)
    text = Column(Text, nullable=True)
    sentiment = Column(String(50), nullable=True)
    risk_level = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class RiskAssessment(Base):
    __tablename__ = "risk_assessments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    risk_level = Column(String(20), nullable=False)
    reason = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    event = Column(String(200), nullable=False)
    risk_level = Column(String(20), nullable=True)
    action = Column(String(200), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class HumanReferral(Base):
    __tablename__ = "human_referrals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    risk_level = Column(String(20), nullable=False)
    reason = Column(Text, nullable=True)
    status = Column(String(30), default="Pending Review")
    created_at = Column(DateTime, default=datetime.utcnow)

class PrivacySettings(Base):
    __tablename__ = "privacy_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, nullable=False)

    save_journal = Column(Integer, default=1)
    enable_sentiment = Column(Integer, default=1)
    enable_facial_analysis = Column(Integer, default=0)
    share_with_staff = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)