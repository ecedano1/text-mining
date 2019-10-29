import praw
import configparser
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#used for measuring the intensity of the natural language of humans 

# VG_dict= {'Text-Mining/reddit_comment.txt'}

# config= configparser.ConfigParser()
# config.read_dict()

reddit = praw.Reddit(client_id='1RjIws9QcWKMww',
                     client_secret='-K-88s47llEE3_1FASt-ey_UHZ4',
                     username='ecedano1',
                     password='ECedano11!',
                     user_agent= 'windows:com.pythonsentimentapp.myredditapp:v1.2.3 (by/u/ecedano1)')

sub = 'learnpython'
submissions = reddit.subreddit(sub).top('day', limit=5)
top5 = [(submission.title, submission.selftext) for submission in submissions]


