from app.safety.tool_executor import execute_tool


print("Normal tool:")
print(execute_tool("get_user_mood"))


print("\nReferral WITHOUT approval:")
print(execute_tool("create_referral"))


print("\nReferral WITH approval:")
print(execute_tool("create_referral", approved=True))


print("\nUnknown tool:")
print(execute_tool("delete_user_data"))