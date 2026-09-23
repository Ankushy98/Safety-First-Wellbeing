def baseline_risk(mood, sentiment):
    """
    Simple baseline risk system.
    This is only for evaluation comparison.
    """

    if mood <= 2 and sentiment == "Negative":
        return "MEDIUM"

    return "LOW"


test_cases = [
    {"mood": 4, "sentiment": "Positive"},
    {"mood": 3, "sentiment": "Neutral"},
    {"mood": 2, "sentiment": "Negative"},
    {"mood": 5, "sentiment": "Positive"},
    {"mood": 1, "sentiment": "Negative"},
]


print("===== BASELINE EVALUATION =====")

for case in test_cases:

    result = baseline_risk(
        mood=case["mood"],
        sentiment=case["sentiment"]
    )

    print(
        f"Mood: {case['mood']} | "
        f"Sentiment: {case['sentiment']} | "
        f"Risk: {result}"
    )