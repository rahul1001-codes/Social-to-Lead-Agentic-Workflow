def detect_intent(user_input):
    user_input = user_input.lower()

    if any(x in user_input for x in [
        "buy", "subscribe", "sign up", "try", "interested", "i want"
    ]):
        return "high_intent"

    elif any(x in user_input for x in [
        "price", "pricing", "cost", "plan", "plans",
        "feature", "features", "subscription", "how much"
    ]):
        return "pricing"

    elif any(x in user_input for x in ["hi", "hello", "hey"]):
        return "greeting"

    return "unknown"


