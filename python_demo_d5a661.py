# Learning Objective:
# This tutorial will guide you through building a basic text sentiment analyzer
# using Python's Natural Language Toolkit (NLTK) library. We will focus on
# understanding how to preprocess text and use a pre-trained sentiment
# analysis model to classify text as positive, negative, or neutral.
# This is a fundamental step in many Natural Language Processing (NLP) tasks.

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# --------------------------------------------------------------------------
# Step 1: Download necessary NLTK data
# --------------------------------------------------------------------------
# NLTK requires certain data packages to be downloaded for specific functions.
# The 'vader_lexicon' is a lexicon and rule-based sentiment analysis tool
# that is specifically attuned to sentiments expressed in social media.
# We use a try-except block to avoid re-downloading if it's already present.

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except nltk.downloader.DownloadError:
    print("Downloading NLTK vader_lexicon...")
    nltk.download('vader_lexicon')
    print("Download complete.")
except LookupError:
    print("Downloading NLTK vader_lexicon (LookupError)...")
    nltk.download('vader_lexicon')
    print("Download complete.")

# --------------------------------------------------------------------------
# Step 2: Initialize the Sentiment Intensity Analyzer
# --------------------------------------------------------------------------
# The SentimentIntensityAnalyzer is the core tool from NLTK for sentiment analysis.
# It's a pre-trained model that can analyze the sentiment of text without us
# needing to train a model from scratch for this basic example.
sia = SentimentIntensityAnalyzer()

# --------------------------------------------------------------------------
# Step 3: Define a function to analyze sentiment
# --------------------------------------------------------------------------
# This function will take a piece of text, analyze its sentiment, and
# return a classification (positive, negative, or neutral) along with
# the sentiment scores.

def analyze_sentiment(text: str) -> dict:
    """
    Analyzes the sentiment of a given text using NLTK's VADER.

    Args:
        text: The input string to analyze.

    Returns:
        A dictionary containing:
        - 'scores': A dictionary of polarity scores (neg, neu, pos, compound).
        - 'classification': A string indicating 'Positive', 'Negative', or 'Neutral'.
    """
    # The polarity_scores() method returns a dictionary of scores.
    # 'neg': Negative sentiment score
    # 'neu': Neutral sentiment score
    # 'pos': Positive sentiment score
    # 'compound': A normalized, weighted composite score that is the most
    #             commonly used metric for overall sentiment. It ranges
    #             from -1 (most negative) to +1 (most positive).
    scores = sia.polarity_scores(text)

    # Determine the overall classification based on the compound score.
    # These thresholds are commonly used with VADER:
    # - compound >= 0.05  => Positive
    # - compound <= -0.05 => Negative
    # - otherwise         => Neutral
    if scores['compound'] >= 0.05:
        classification = 'Positive'
    elif scores['compound'] <= -0.05:
        classification = 'Negative'
    else:
        classification = 'Neutral'

    return {
        'scores': scores,
        'classification': classification
    }

# --------------------------------------------------------------------------
# Step 4: Example Usage
# --------------------------------------------------------------------------
# Let's test our sentiment analyzer with a few example sentences.
# This demonstrates how to use the function we created.

if __name__ == "__main__":
    print("--- Sentiment Analyzer Demonstration ---")

    # Example 1: Clearly positive text
    text1 = "I love this new movie! It's absolutely fantastic and I highly recommend it."
    result1 = analyze_sentiment(text1)
    print(f"\nText: '{text1}'")
    print(f"  Sentiment Scores: {result1['scores']}")
    print(f"  Overall Sentiment: {result1['classification']}")

    # Example 2: Clearly negative text
    text2 = "This product is terrible. It broke after only one use and was a complete waste of money."
    result2 = analyze_sentiment(text2)
    print(f"\nText: '{text2}'")
    print(f"  Sentiment Scores: {result2['scores']}")
    print(f"  Overall Sentiment: {result2['classification']}")

    # Example 3: Neutral text
    text3 = "The weather today is partly cloudy with a chance of rain in the afternoon."
    result3 = analyze_sentiment(text3)
    print(f"\nText: '{text3}'")
    print(f"  Sentiment Scores: {result3['scores']}")
    print(f"  Overall Sentiment: {result3['classification']}")

    # Example 4: Mixed sentiment text (VADER is good at handling this)
    text4 = "The service was okay, but the food was amazing!"
    result4 = analyze_sentiment(text4)
    print(f"\nText: '{text4}'")
    print(f"  Sentiment Scores: {result4['scores']}")
    print(f"  Overall Sentiment: {result4['classification']}")

    # Example 5: A slightly more nuanced example
    text5 = "I'm not sure if I liked it, it was okay I guess."
    result5 = analyze_sentiment(text5)
    print(f"\nText: '{text5}'")
    print(f"  Sentiment Scores: {result5['scores']}")
    print(f"  Overall Sentiment: {result5['classification']}")