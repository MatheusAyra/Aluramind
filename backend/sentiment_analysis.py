from textblob import TextBlob

def classify_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return "POSITIVO"
    elif analysis.sentiment.polarity < -0.1:
        return "NEGATIVO"
    return "INCONCLUSIVO"
