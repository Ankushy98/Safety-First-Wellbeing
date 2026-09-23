def evaluate_risk(mood, sentiment, crisis_detected):
    """
    Demo safety triage logic.
    This is a workflow classification, not a medical diagnosis.
    """

    if crisis_detected:
        return "HIGH"

    if mood <= 2 and sentiment == "Negative":
        return "MEDIUM"

    return "LOW"


test_cases = [
    {
        "name": "Normal positive case",
        "mood": 4,
        "sentiment": "Positive",
        "crisis_detected": False,
        "expected": "LOW"
    },
    {
        "name": "Low mood + negative sentiment",
        "mood": 2,
        "sentiment": "Negative",
        "crisis_detected": False,
        "expected": "MEDIUM"
    },
    {
        "name": "Safety rule test",
        "mood": 3,
        "sentiment": "Negative",
        "crisis_detected": True,
        "expected": "HIGH"
    },
    {
        "name": "Neutral case",
        "mood": 3,
        "sentiment": "Neutral",
        "crisis_detected": False,
        "expected": "LOW"
    }
]


print("===== SAFETY EVALUATION =====")

correct = 0

for case in test_cases:

    predicted = evaluate_risk(
        mood=case["mood"],
        sentiment=case["sentiment"],
        crisis_detected=case["crisis_detected"]
    )

    if predicted == case["expected"]:
        result = "PASS"
        correct += 1
    else:
        result = "FAIL"

    print(
        f"{case['name']} | "
        f"Expected: {case['expected']} | "
        f"Predicted: {predicted} | "
        f"{result}"
    )


accuracy = correct / len(test_cases)

print()
print(f"Correct: {correct}/{len(test_cases)}")
print(f"Accuracy: {accuracy:.2%}")