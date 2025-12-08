import tweepy
import os
from dotenv import load_dotenv

load_dotenv() # Loads .env file

def create_client():
    """
    Create and return a Tweepy client using the Bearer Token.
    """

    bearer_token = os.getenv("BEARER_TOKEN")
    if not bearer_token:
        raise ValueError("Bearer token not found. Please set it in .env")

    return tweepy.Client(
        bearer_token=bearer_token,
        wait_on_rate_limit=True # Needed for free access X API
        )
