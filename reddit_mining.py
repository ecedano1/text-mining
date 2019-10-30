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

sub = 'modernwarfare'
submissions = reddit.subreddit(sub).hot(limit = 2)
# top('day', limit=5)
top2 = [(submission.title, submission.selftext) for submission in submissions]


for title, text in top2: 
    print (title, text)

# sentence = f/open
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)


# ######################### FOR REDDIT POSTING ##################################

# import praw
# import configparser
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer 


# reddit = praw.Reddit(client_id='EXAMPLE',
#                     client_secret='EXAMPLE',
#                     username='EXAMPLE',
#                     password='EXAMPLE',
#                     user_agent= 'EXAMPLE')

# sub = 'learnpython'
# submissions = reddit.subreddit(sub).search('modernwarfare', sort='new', time_filter= 'day', limit = 10)
# # top('day', limit=5)
# top10 = [(submission.title, submission.selftext) for submission in submissions]

# for title, text in top10: 
#     print (title)

# # sentence = f/open
# # score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# # print(score)
