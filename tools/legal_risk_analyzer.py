def legal_risk(text):
    keywords = ["violence", "dowry", "rape", "threat"]
    return min(sum(2 for w in keywords if w in text.lower()), 10)