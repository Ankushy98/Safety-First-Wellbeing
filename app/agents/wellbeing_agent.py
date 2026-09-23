from ..safety.tool_policy import check_tool_permission
from ..safety.approval_gate import request_approval


class WellbeingAgent:

    def request_tool(self, tool_name: str, user_id: int):

        permission = check_tool_permission(tool_name)

        if not permission["allowed"]:
            return {
                "status": "BLOCKED",
                "tool": tool_name,
                "user_id": user_id,
                "reason": "Tool is not allowed"
            }

        approval = request_approval(tool_name)

        if approval["status"] == "PENDING_APPROVAL":
            return {
                "status": "PENDING_APPROVAL",
                "tool": tool_name,
                "user_id": user_id,
                "reason": "Human approval required"
            }

        return {
            "status": "APPROVED",
            "tool": tool_name,
            "user_id": user_id,
            "reason": "Tool can be used"
        }