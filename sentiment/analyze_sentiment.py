from textblob import TextBlob

def get_emotion(text):
    if not text.strip():
        return "neutral"

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Emotion mapping logic
    if polarity > 0.5:
        return "happy"
    elif polarity > 0.2:
        return "romantic"
    elif polarity < -0.5:
        return "angry"
    elif polarity < -0.3:
        return "sad"
    elif subjectivity < 0.3:
        return "neutral"
    else:
        return "calm"
