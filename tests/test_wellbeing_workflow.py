from app.agents.wellbeing_agent import WellbeingAgent


agent = WellbeingAgent()

print("\nLOW RISK")
print(agent.generate_support_action(
    user_id=1,
    risk_level="LOW",
    sentiment="Positive"
))


print("\nMEDIUM RISK")
print(agent.generate_support_action(
    user_id=1,
    risk_level="MEDIUM",
    sentiment="Negative"
))


print("\nHIGH RISK")
print(agent.generate_support_action(
    user_id=1,
    risk_level="HIGH",
    sentiment="Negative"
))