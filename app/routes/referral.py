from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..database.models import HumanReferral
from ..safety.auth import verify_admin_key


router = APIRouter(
    prefix="/referral",
    tags=["Human Referral"]
)


@router.post("/")
def create_referral(
    user_id: int,
    risk_level: str,
    reason: str,
    db: Session = Depends(get_db)
):

    referral = HumanReferral(
        user_id=user_id,
        risk_level=risk_level,
        reason=reason,
        status="Pending Review"
    )

    db.add(referral)
    db.commit()
    db.refresh(referral)

    return {
        "message": "Human referral created successfully",
        "referral_id": referral.id,
        "user_id": referral.user_id,
        "risk_level": referral.risk_level,
        "reason": referral.reason,
        "status": referral.status
    }


@router.get("/")
@router.get("/")
def get_referrals(
    db: Session = Depends(get_db),
    _: bool = Depends(verify_admin_key)
):

    referrals = (
        db.query(HumanReferral)
        .order_by(HumanReferral.created_at.desc())
        .all()
    )

    return referrals