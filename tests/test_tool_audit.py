from app.database.database import SessionLocal
from app.database.models import AuditLog
from app.safety.tool_executor import execute_tool


db = SessionLocal()

try:
    print("Normal tool:")
    print(
        execute_tool(
            "get_user_mood",
            user_id=1,
            db=db
        )
    )

    print("\nReferral without approval:")
    print(
        execute_tool(
            "create_referral",
            user_id=1,
            db=db
        )
    )

    print("\nReferral with approval:")
    print(
        execute_tool(
            "create_referral",
            user_id=1,
            db=db,
            approved=True
        )
    )

    print("\nUnknown tool:")
    print(
        execute_tool(
            "delete_user_data",
            user_id=1,
            db=db
        )
    )

    print("\n--- AUDIT LOGS ---")

    logs = (
        db.query(AuditLog)
        .order_by(AuditLog.id.desc())
        .limit(10)
        .all()
    )

    for log in logs:
        print(
            log.id,
            "| User:",
            log.user_id,
            "| Event:",
            log.event,
            "| Action:",
            log.action
        )

finally:
    db.close()