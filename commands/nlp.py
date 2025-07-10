

# commands/nlp.py

def handle_nlp(action, param1, param2):
    print("Command in nlp.py handler:", action, param1, param2)

    if action == "analyze_sentiment":
        return analyze_sentiment(param1)

    return f"[nlp.py] Unknown action: {action}"

def handle_t555(action, param1, param2):
    return analyze_sentiment(param1)

def analyze_sentiment(text):
    positive = ["좋아", "행복", "기뻐", "좋다", "사랑"]
    negative = ["싫어", "화나", "짜증", "우울", "나빠"]

    score = 0
    for word in positive:
        if word in text:
            score += 1
    for word in negative:
        if word in text:
            score -= 1

    if score > 0:
        return "긍정적인 감정으로 분석됨 🙂"
    elif score < 0:
        return "부정적인 감정으로 분석됨 🙁"
    else:
        return "중립적인 감정으로 분석됨 😐"

