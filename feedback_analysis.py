def positive_feedback(ratings):
    if not ratings:
        return "No ratings available."
    positive = [r for r in ratings if r >= 4]
    percent = (len(positive) / len(ratings)) * 100
    return f"Positive Feedback: {round(percent, 2)}%"

# Example
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(positive_feedback(ratings))
