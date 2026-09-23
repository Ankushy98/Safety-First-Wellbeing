from .tool_policy import check_tool_permission


def request_approval(tool_name: str):
    permission = check_tool_permission(tool_name)

    if not permission["allowed"]:
        return {
            "status": "BLOCKED",
            "tool": tool_name,
            "message": "Tool is not allowed"
        }

    if permission["requires_approval"]:
        return {
            "status": "PENDING_APPROVAL",
            "tool": tool_name,
            "message": "Human approval is required"
        }

    return {
        "status": "APPROVED",
        "tool": tool_name,
        "message": "No human approval required"
    }


def process_approval(
    tool_name: str,
    decision: str,
    user_id: int = None
):
    if decision not in ["Approved", "Rejected"]:
        return {
            "status": "INVALID",
            "message": "Decision must be Approved or Rejected"
        }

    if decision == "Approved":
        status = "APPROVED"
        message = "Human approved the tool action"
    else:
        status = "REJECTED"
        message = "Human rejected the tool action"

    return {
        "status": status,
        "tool": tool_name,
        "user_id": user_id,
        "message": message
    }