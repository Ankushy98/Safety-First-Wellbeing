def check_crisis_signal(text: str) -> bool:
    """
    Deterministic safety rule.
    Returns True when a predefined development safety-test token is detected.
    """

    if not text:
        return False

    text = text.upper()

    # Development/testing token.
    # In production, this should be replaced by an institutionally
    # reviewed safety lexicon and policy.
    if "CRISIS_TEST" in text:
        return True

    return False