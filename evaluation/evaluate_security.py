from app.safety.tool_policy import check_tool_permission


test_cases = [
    {
        "tool": "get_user_mood",
        "expected_allowed": True
    },
    {
        "tool": "get_recent_journal",
        "expected_allowed": True
    },
    {
        "tool": "create_referral",
        "expected_allowed": True
    },
    {
        "tool": "delete_user_data",
        "expected_allowed": False
    },
    {
        "tool": "access_private_files",
        "expected_allowed": False
    }
]


print("===== SECURITY EVALUATION =====")

passed = 0

for case in test_cases:

    result = check_tool_permission(case["tool"])

    actual = result["allowed"]
    expected = case["expected_allowed"]

    if actual == expected:
        status = "PASS"
        passed += 1
    else:
        status = "FAIL"

    print(
        f"Tool: {case['tool']} | "
        f"Expected: {expected} | "
        f"Actual: {actual} | "
        f"{status}"
    )


print()
print(f"Passed: {passed}/{len(test_cases)}")
print(f"Failed: {len(test_cases) - passed}/{len(test_cases)}")