from tweetscrape.profile_tweets import TweetScrapperProfile

tweet_scrapper = TweetScrapperProfile("", 40, 'twitter.csv', 'csv')
tweet_count, tweet_id, tweet_time, dump_path = tweet_scrapper.get_profile_tweets()
print("Extracted {0} tweets till {1} at {2}".format(tweet_count, tweet_time, dump_path))
