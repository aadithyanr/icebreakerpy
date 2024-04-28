from langchain_community.document_loaders import TwitterTweetLoader
import os
import tweepy
import logging

logger = logging.getLogger("twitter")
auth = tweepy.OAuthHandler(
    os.environ["TWITTER_API_KEY"],
    os.environ["TWITTER_API_SECRET"],
)
auth.set_access_token(
    os.environ["TWITTER_ACCESS_TOKEN"],
    os.environ["TWITTER_ACCESS_SECRET"],
)
api = tweepy.API(auth)
