from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from app.models.sentiment import analyze_sentiment


test_cases = [
    ("I had a wonderful and happy day", "Positive"),
    ("I am feeling very sad and unhappy", "Negative"),
    ("Today was an ordinary day", "Neutral"),
    ("I really enjoyed my day", "Positive"),
    ("I feel terrible and disappointed", "Negative"),
    ("I went to college today", "Neutral"),
]


y_true = []
y_pred = []

print("===== SENTIMENT METRICS =====")

for text, expected in test_cases:

    predicted = analyze_sentiment(text)

    y_true.append(expected)
    y_pred.append(predicted)

    print(
        f"Text: {text} | "
        f"Expected: {expected} | "
        f"Predicted: {predicted}"
    )


accuracy = accuracy_score(y_true, y_pred)

precision = precision_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

recall = recall_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

f1 = f1_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

cm = confusion_matrix(
    y_true,
    y_pred,
    labels=["Negative", "Neutral", "Positive"]
)


print()
print("===== RESULTS =====")
print(f"Accuracy : {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall   : {recall:.2%}")
print(f"F1-Score : {f1:.2%}")

print()
print("Confusion Matrix")
print("Labels: Negative, Neutral, Positive")
print(cm)