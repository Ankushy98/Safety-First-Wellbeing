from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database.models import AuditLog

from ..database.database import get_db
from ..database.models import AuditLog, HumanReferral
from ..audit.audit_logger import create_audit_log
from ..safety.auth import verify_admin_key


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


class ReferralReview(BaseModel):
    decision: str


@router.get("/audit-logs")
def get_audit_logs(
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin_key)
):
    logs = (
        db.query(AuditLog)
        .order_by(AuditLog.created_at.desc())
        .all()
    )

    return logs


@router.put("/referrals/{referral_id}/review")
def review_referral(
    referral_id: int,
    review: ReferralReview,
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin_key)
):

    if review.decision not in ["Approved", "Rejected"]:
        raise HTTPException(
            status_code=400,
            detail="Decision must be Approved or Rejected"
        )

    referral = (
        db.query(HumanReferral)
        .filter(HumanReferral.id == referral_id)
        .first()
    )

    if not referral:
        raise HTTPException(
            status_code=404,
            detail="Referral not found"
        )

    if referral.status != "Pending Review":
        raise HTTPException(
            status_code=400,
            detail="Referral has already been reviewed"
        )

    referral.status = review.decision

    db.commit()
    db.refresh(referral)

    create_audit_log(
        db=db,
        user_id=referral.user_id,
        event="Human referral reviewed",
        risk_level=referral.risk_level,
        action=f"Human decision: {review.decision}"
    )

    return {
        "message": "Referral review completed",
        "referral_id": referral.id,
        "status": referral.status,
        "reviewed_by": "Human Staff"
    }

@router.get("/monitoring")
def get_monitoring(
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin_key)
):

    total_logs = db.query(AuditLog).count()

    high_risk = (
        db.query(AuditLog)
        .filter(AuditLog.risk_level == "HIGH")
        .count()
    )

    blocked_tools = (
        db.query(AuditLog)
        .filter(AuditLog.event == "Tool blocked")
        .count()
    )

    agent_decisions = (
        db.query(AuditLog)
        .filter(AuditLog.event == "Agent decision")
        .count()
    )

    return {
        "total_audit_logs": total_logs,
        "high_risk_events": high_risk,
        "blocked_tool_actions": blocked_tools,
        "agent_decisions": agent_decisions
    }