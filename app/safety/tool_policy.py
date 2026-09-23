ALLOWED_TOOLS = {
    "get_user_mood": {
        "requires_approval": False
    },

    "get_recent_journal": {
        "requires_approval": False
    },

    "generate_support_message": {
        "requires_approval": False
    },

    "create_referral": {
        "requires_approval": True
    }
}


def check_tool_permission(tool_name: str):
    if tool_name not in ALLOWED_TOOLS:
        return {
            "allowed": False,
            "requires_approval": False,
            "reason": "Tool is not allowed"
        }

    tool = ALLOWED_TOOLS[tool_name]

    return {
        "allowed": True,
        "requires_approval": tool["requires_approval"],
        "reason": "Tool is allowed"
    }