# Version 1: Oct 1, 2025

import tweepy
from textblob import TextBlob

# Step 1 – Authenticate with your Bearer Token
bearer_token = "INSERT_BEARER_TOKEN"

# Create Tweepy client for API v2
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Step 2 – Define search query
query = "Open AI -is:retweet lang:en"

# Request tweets including author info and timestamp
tweets = client.search_recent_tweets(
    query=query,
    max_results=20,
    tweet_fields=["created_at", "author_id", "id", "text"],
    expansions=["author_id"],
    user_fields=["username"]
)

# Build a map of user_id -> username
users = {user.id: user.username for user in tweets.includes['users']} if tweets.includes else {}

# Step 3 – Print each tweet with author, timestamp, and sentiment
if tweets.data:
    for tweet in tweets.data:
        text = tweet.text
        author = users.get(tweet.author_id, "Unknown")
        timestamp = tweet.created_at
        tweet_url = f"https://twitter.com/{author}/status/{tweet.id}"

        # Sentiment analysis
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = "positive"
        elif polarity < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        print(f"Author: @{author}")
        print(f"Timestamp: {timestamp}")
        print(f"Tweet: {text}")
        print(f"Polarity: {polarity:.2f} → {sentiment}")
        print(f"Link: {tweet_url}")
        print("-" * 80)
else:
    print("No tweets found for your query.")
