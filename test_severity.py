def get_severity(text):

    text = text.lower()

    high_keywords = [
        "fraud",
        "scam",
        "identity theft",
        "unauthorized",
        "stolen",
        "lawsuit",
        "harassment",
        "threat",
        "illegal"
    ]

    medium_keywords = [
        "charged",
        "delay",
        "issue",
        "problem",
        "error",
        "incorrect",
        "dispute"
    ]

    high_score = 0
    medium_score = 0

    for word in high_keywords:

        if word in text:
            high_score += 2

    for word in medium_keywords:

        if word in text:
            medium_score += 1

    if high_score >= 2:
        return "High"

    elif medium_score >= 1:
        return "Medium"

    else:
        return "Low"