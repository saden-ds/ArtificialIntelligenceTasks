from transformers import pipeline
import re

sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment", device=0)

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

neutral_keywords = [
    "neitrāls", "nekas īpašs", "parasts", "vidējs", "tikai", "normāls", "nekas īpašs", "bez emocijām"
]

def get_sentiment(sentence):
    if any(re.search(r'\b' + re.escape(keyword) + r'\b', sentence.lower()) for keyword in neutral_keywords):
        return 'Neitrāls'
    
    result = sentiment_analyzer(sentence)
    sentiment = result[0]['label']
    if sentiment == '5 stars':
        return 'Pozitīvs'
    elif sentiment == '1 star':
        return 'Negatīvs'
    else:
        return 'Neitrāls'

for sentence in sentences:
    sentiment = get_sentiment(sentence)
    print(f"Teikums: {sentence}\nNoskaņojums: {sentiment}\n")
