from app.agents.wellbeing_agent import WellbeingAgent


agent = WellbeingAgent()


print("Normal tool:")
print(
    agent.request_tool(
        "get_user_mood",
        user_id=1
    )
)


print("\nSensitive tool:")
print(
    agent.request_tool(
        "create_referral",
        user_id=1
    )
)


print("\nBlocked tool:")
print(
    agent.request_tool(
        "delete_user_data",
        user_id=1
    )
)