from app.models.sentiment import analyze_sentiment


test_inputs = [
    "",
    "   ",
    "I am happy today",
    "I am very sad today",
    "123456789",
    "!!! ???",
    "Today was okay."
]


print("===== ROBUSTNESS TEST =====")

passed = 0

for text in test_inputs:

    try:
        result = analyze_sentiment(text)

        print(
            f"Input: {repr(text)} | "
            f"Output: {result} | PASS"
        )

        passed += 1

    except Exception as e:

        print(
            f"Input: {repr(text)} | "
            f"ERROR: {e} | FAIL"
        )


print()
print(f"Passed: {passed}/{len(test_inputs)}")
print(f"Failed: {len(test_inputs) - passed}/{len(test_inputs)}")