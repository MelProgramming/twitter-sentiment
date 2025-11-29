# Version 2: Nov 9, 2025 WIP

from twitter_client import create_client
from textblob import TextBlob
from utils import clean_text
import csv
from typing import List

def fetch_tweets(query: str, max_results: int = 10) -> List[str]:
    """
    Fetch recent tweets containing the given query.
    Returns a list of tweet texts.
    """
    client = create_client()
    tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["lang"])
    if tweets and tweets.data:
        return [t.text for t in tweets.data if t.lang == "en"]
    return []
    # return [t.text for t in tweets.data if t.lang == "en"] if tweets.data else []

def analyze_sentiment(text: str) -> float:
    """
    Return the polarity score of a given text using TextBlob.
    Positive (>0), Neutral (0), Negative (<0).
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def main() -> None:
    query = input("Enter a search term or hashtag: ")
    tweets = fetch_tweets(query)

    results = []
    for tweet in tweets:
        cleaned = clean_text(tweet)
        polarity = analyze_sentiment(cleaned)
        sentiment = (
            "Positive" if polarity > 0
            else "Negative" if polarity < 0
            else "Neutral"
        )
        results.append((cleaned, sentiment, round(polarity, 3)))

    # Save to CSV
    with open("sentiment_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tweet", "Sentiment", "Polarity"])
        writer.writerows(results)

    print(f"{len(results)} tweets analyzed. Results saved to sentiment_results.csv")

if __name__ == "__main__":
    main()
