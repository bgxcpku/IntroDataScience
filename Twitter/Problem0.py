"""
Json read of tweets related to the search term microsoft.
"""
import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
dd_tweets = json.load(response)

# print json.dumps(dd_tweets, indent=4)

for d_tweet in dd_tweets['results']:
    s_tweet_text = d_tweet["text"]
    s_tweet_text = s_tweet_text.encode('utf-8')
    print s_tweet_text
