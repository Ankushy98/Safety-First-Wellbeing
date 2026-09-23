from app.safety.approval_gate import (
    request_approval,
    process_approval
)


print("Normal tool:")
print(request_approval("get_user_mood"))

print("\nReferral tool:")
print(request_approval("create_referral"))

print("\nUnknown tool:")
print(request_approval("delete_user_data"))

print("\nHuman approves referral:")
print(process_approval("create_referral", "Approved"))

print("\nHuman rejects referral:")
print(process_approval("create_referral", "Rejected"))