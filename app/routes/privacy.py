from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..database.models import PrivacySettings


router = APIRouter(
    prefix="/privacy",
    tags=["Privacy"]
)


class PrivacyUpdate(BaseModel):
    save_journal: bool = True
    enable_sentiment: bool = True
    enable_facial_analysis: bool = False
    share_with_staff: bool = False


@router.get("/{user_id}")
def get_privacy_settings(
    user_id: int,
    db: Session = Depends(get_db)
):
    settings = (
        db.query(PrivacySettings)
        .filter(PrivacySettings.user_id == user_id)
        .first()
    )

    if not settings:
        settings = PrivacySettings(user_id=user_id)
        db.add(settings)
        db.commit()
        db.refresh(settings)

    return {
        "user_id": settings.user_id,
        "save_journal": bool(settings.save_journal),
        "enable_sentiment": bool(settings.enable_sentiment),
        "enable_facial_analysis": bool(settings.enable_facial_analysis),
        "share_with_staff": bool(settings.share_with_staff)
    }


@router.put("/{user_id}")
def update_privacy_settings(
    user_id: int,
    privacy: PrivacyUpdate,
    db: Session = Depends(get_db)
):
    settings = (
        db.query(PrivacySettings)
        .filter(PrivacySettings.user_id == user_id)
        .first()
    )

    if not settings:
        settings = PrivacySettings(user_id=user_id)
        db.add(settings)

    settings.save_journal = int(privacy.save_journal)
    settings.enable_sentiment = int(privacy.enable_sentiment)
    settings.enable_facial_analysis = int(privacy.enable_facial_analysis)
    settings.share_with_staff = int(privacy.share_with_staff)

    db.commit()
    db.refresh(settings)

    return {
        "message": "Privacy settings updated successfully",
        "user_id": settings.user_id,
        "save_journal": bool(settings.save_journal),
        "enable_sentiment": bool(settings.enable_sentiment),
        "enable_facial_analysis": bool(settings.enable_facial_analysis),
        "share_with_staff": bool(settings.share_with_staff)
    }