# app.py

from flask import Flask
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Sentiment Analysis API!"


@app.route('/analyze_sentiment/<text>')
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"


if __name__ == '__main__':
    app.run(debug=True)
