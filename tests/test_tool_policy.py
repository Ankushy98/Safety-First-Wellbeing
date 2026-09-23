from app.safety.tool_policy import check_tool_permission


print("Allowed tool:")
print(check_tool_permission("get_user_mood"))

print("\nReferral tool:")
print(check_tool_permission("create_referral"))

print("\nBlocked tool:")
print(check_tool_permission("delete_user_data"))