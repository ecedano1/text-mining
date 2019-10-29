import praw
import configparser
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#used for measuring the intensity of the natural language of humans 

# VG_Sentiment_dict= {}

config= configparser.ConfigParser()
# config.read_dict()

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)
sub = 'learnpython'
submissions = reddit.subreddit(sub).top('day', limit=5)
top5 = [(submission.title, submission.selftext) for submission in submissions]


