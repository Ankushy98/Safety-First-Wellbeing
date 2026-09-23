def calculate_risk(mood: int, sentiment: str, crisis_detected: bool) -> str:
    """
    Simple rule-based risk triage.
    This is a workflow classification, not a medical diagnosis.
    """

    # Safety rule always takes priority
    if crisis_detected:
        return "HIGH"

    # Medium-risk indicators
    if mood <= 2 and sentiment == "Negative":
        return "MEDIUM"

    # Otherwise
    return "LOW"