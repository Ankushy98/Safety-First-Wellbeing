from sqlalchemy.orm import Session

from ..database.models import AuditLog


def create_audit_log(
    db: Session,
    user_id: int,
    event: str,
    risk_level: str = None,
    action: str = None
):
    log = AuditLog(
        user_id=user_id,
        event=event,
        risk_level=risk_level,
        action=action
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log