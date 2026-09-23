from sqlalchemy.orm import Session

from .tool_policy import check_tool_permission
from ..audit.audit_logger import create_audit_log


def execute_tool(
    tool_name: str,
    user_id: int,
    db: Session,
    approved: bool = False
):

    permission = check_tool_permission(tool_name)

    if not permission["allowed"]:

        create_audit_log(
            db=db,
            user_id=user_id,
            event="Tool blocked",
            risk_level=None,
            action=f"Blocked unauthorized tool: {tool_name}"
        )

        return {
            "status": "BLOCKED",
            "tool": tool_name,
            "message": "Tool is not allowed"
        }

    if permission["requires_approval"] and not approved:

        create_audit_log(
            db=db,
            user_id=user_id,
            event="Tool approval required",
            risk_level=None,
            action=f"Approval required for: {tool_name}"
        )

        return {
            "status": "BLOCKED",
            "tool": tool_name,
            "message": "Human approval required before execution"
        }

    if tool_name == "get_user_mood":
        result = "Mood data retrieved"

    elif tool_name == "get_recent_journal":
        result = "Recent journal retrieved"

    elif tool_name == "generate_support_message":
        result = "Support message generated"

    elif tool_name == "create_referral":
        result = "Human referral action executed"

    else:
        return {
            "status": "BLOCKED",
            "tool": tool_name,
            "message": "Unknown tool"
        }

    create_audit_log(
        db=db,
        user_id=user_id,
        event="Tool executed",
        risk_level=None,
        action=f"Executed tool: {tool_name}"
    )

    return {
        "status": "EXECUTED",
        "tool": tool_name,
        "result": result
    }