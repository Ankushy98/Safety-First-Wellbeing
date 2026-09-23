from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..database.models import JournalEntry, HumanReferral, PrivacySettings
from ..models.sentiment import analyze_sentiment
from ..models.risk_model import calculate_risk
from ..safety.crisis_rules import check_crisis_signal
from ..audit.audit_logger import create_audit_log


router = APIRouter(
    prefix="/journal",
    tags=["Journal"]
)


class JournalCreate(BaseModel):
    user_id: int
    mood: int = Field(..., ge=1, le=5)
    text: str | None = None


@router.post("/")
def create_journal(
    journal: JournalCreate,
    db: Session = Depends(get_db)
):

    # 1. Get user's privacy settings
    settings = (
        db.query(PrivacySettings)
        .filter(PrivacySettings.user_id == journal.user_id)
        .first()
    )

    # Create default settings if user has none
    if not settings:
        settings = PrivacySettings(user_id=journal.user_id)
        db.add(settings)
        db.commit()
        db.refresh(settings)

    # 2. Check crisis safety rule
    crisis_detected = check_crisis_signal(journal.text)

    # 3. Sentiment analysis according to privacy setting
    if settings.enable_sentiment:
        sentiment = analyze_sentiment(journal.text)
    else:
        sentiment = "Disabled"

    # 4. Risk triage
    risk_level = calculate_risk(
        mood=journal.mood,
        sentiment=sentiment,
        crisis_detected=crisis_detected
    )

    # 5. Save journal only if user allowed it
    journal_id = None

    if settings.save_journal:
        entry = JournalEntry(
            user_id=journal.user_id,
            mood=journal.mood,
            text=journal.text,
            sentiment=sentiment,
            risk_level=risk_level
        )

        db.add(entry)
        db.commit()
        db.refresh(entry)

        journal_id = entry.id

    # 6. Create human referral for HIGH risk
    referral_id = None

    if risk_level == "HIGH":
        referral = HumanReferral(
            user_id=journal.user_id,
            risk_level="HIGH",
            reason="Safety rule triggered",
            status="Pending Review"
        )

        db.add(referral)
        db.commit()
        db.refresh(referral)

        referral_id = referral.id

    # 7. Audit log
    create_audit_log(
        db=db,
        user_id=journal.user_id,
        event="Journal analyzed",
        risk_level=risk_level,
        action="Risk triage completed"
    )

    return {
        "message": "Journal processed successfully",
        "journal_id": journal_id,
        "user_id": journal.user_id,
        "mood": journal.mood,
        "sentiment": sentiment,
        "risk_level": risk_level,
        "referral_id": referral_id
    }
@router.get("/summary/{user_id}")
@router.get("/summary/{user_id}")
def get_journal_summary(
    user_id: int,
    db: Session = Depends(get_db)
):
    entries = (
        db.query(JournalEntry)
        .filter(JournalEntry.user_id == user_id)
        .all()
    )

    if not entries:
        return {
            "user_id": user_id,
            "total_entries": 0,
            "average_mood": 0,
            "risk_counts": {}
        }

    average_mood = round(
        sum(entry.mood for entry in entries) / len(entries),
        2
    )

    risk_counts = {}

    for entry in entries:
        risk = getattr(entry, "risk_level", None) or "UNKNOWN"
        risk_counts[risk] = risk_counts.get(risk, 0) + 1

    return {
        "user_id": user_id,
        "total_entries": len(entries),
        "average_mood": average_mood,
        "risk_counts": risk_counts
    }
@router.get("/summary/{user_id}")
# summary function


@router.get("/{user_id}")
# history function

@router.get("/{user_id}")
def get_journals(
    user_id: int,
    db: Session = Depends(get_db)
):
    entries = (
        db.query(JournalEntry)
        .filter(JournalEntry.user_id == user_id)
        .order_by(JournalEntry.created_at.desc())
        .all()
    )

    return entries

@router.get("/summary/{user_id}")
def get_journal_summary(
    user_id: int,
    db: Session = Depends(get_db)
):
    entries = (
        db.query(JournalEntry)
        .filter(JournalEntry.user_id == user_id)
        .order_by(JournalEntry.created_at.asc())
        .all()
    )

    if not entries:
        return {
            "user_id": user_id,
            "total_entries": 0,
            "average_mood": 0,
            "risk_counts": {},
            "message": "No journal entries found"
        }

    average_mood = round(
        sum(entry.mood for entry in entries) / len(entries),
        2
    )

    risk_counts = {}

    for entry in entries:
        risk = entry.risk_level or "UNKNOWN"
        risk_counts[risk] = risk_counts.get(risk, 0) + 1

    return {
        "user_id": user_id,
        "total_entries": len(entries),
        "average_mood": average_mood,
        "risk_counts": risk_counts
    }