from app.safety.tool_policy import check_tool_permission
from app.safety.approval_gate import request_approval


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


    def generate_support_action(
        self,
        user_id: int,
        risk_level: str,
        sentiment: str
    ):

        if risk_level == "HIGH":

            return {
                "status": "HUMAN_REVIEW_REQUIRED",
                "user_id": user_id,
                "risk_level": risk_level,
                "action": "Create human referral",
                "approval_required": True
            }

        if risk_level == "MEDIUM":

            return {
                "status": "SUPPORT",
                "user_id": user_id,
                "risk_level": risk_level,
                "action": "Generate supportive response",
                "approval_required": False
            }

        return {
            "status": "SUPPORT",
            "user_id": user_id,
            "risk_level": risk_level,
            "action": "Provide general wellbeing support",
            "approval_required": False
        }