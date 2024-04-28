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


def scrape_user_tweets(username, num_tweets=5):
    """
    scrapes a twitter user's tweets - basically rips off their whole feed!!??!?!?!?
    each dict has 3 fields - time_posted, text and url
    """
    tweets = api.user_timeline(screen_name=username, count=num_tweets)

    tweet_list = []

    for tweet in tweets:
        for tweet in tweets:
            if "RT @" not in tweet.text and not tweet.text.startswith("@"):
                base_url = "https://x.com/"
                tweet_dict = {}
                tweet_dict["time_posted"] = str(
                    datetime.now(timezone.utc) - tweet.created_at
                )
                tweet_dict["text"] = tweet.text
                screen_name = tweet.user.screen_name
                tweet_dict["url"] = f"{base_url}{screen_name}/status/{tweet.id}"
                tweet_list.append(tweet_dict)

        return tweet_list
