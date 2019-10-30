import praw
import configparser
import nltk
import pandas

from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#used for measuring the intensity of the natural language of humans 

VG_comment= 'Everyone constantly bitches and moans that each new COD is a re-skin of the last.\
    The most innovative COD in a minute drops, and now people just want a re-skin of Black Ops 4.\
        Hopefully Infinity Ward can distinguish in this clown show the legitimate criticism\
            from the people who just spend their entire day bitching\
                on this website just to bitch. Great game IW.\
                    Definitely needs some tweaks like any game that just came out,\
                        but this is one of the best COD games yet.'



reddit = praw.Reddit(client_id='1RjIws9QcWKMww',
                    client_secret='-K-88s47llEE3_1FASt-ey_UHZ4',
                    username='ecedano1',
                    password='ECedano11!',
                    user_agent= 'windows:com.pythonsentimentapp.myredditapp:v1.2.3 (by/u/ecedano1)')

sub = 'modernwarfare'
submissions = reddit.subreddit(sub).new()
# (limit = 20)
# top('day', limit = 5) other functions 
# hot('day', limit = 2)
# new(limit= 3)

top2 = [(submission.title, submission.selftext) for submission in submissions]
# top_level_comments = list(submissions.comments)
# all_comments = submissions.comments.list()

for title, text in top2: 
    print (title, text)

breakpoint()

topics_dict = { "title":[], \
    "score":[],\
        "id":[], "url":[],\
            "comms_num": [], \
                "created": [], \
                    "body":[]}


for submission in submissions:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)


pd = pandas
topics_data = pd.DataFrame(topics_dict)

print(topics_data)


# sentence = VG_dict
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)


# ######################### FOR REDDIT POSTING ##################################

# import praw
# import nltk
# import pandas

# from nltk.sentiment.vader import SentimentIntensityAnalyzer 
# #used for measuring the intensity of the natural language of humans 


# reddit = praw.Reddit(client_id='EXAMPLE',
#                     client_secret='EXAMPLE',
#                     username='EXAMPLE',
#                     password='EXAMPLE',
#                     user_agent= 'EXAMPLE')

# sub = 'modernwarfare'
# submissions = reddit.subreddit(sub).new(limit = 10)
# # (limit = 20)
# # top('day', limit = 5) other versions
# # hot('day', limit = 2)
# # new(limit= 3)

# top2 = [(submission.title, submission.selftext) for submission in submissions]
# # top_level_comments = list(submissions.comments)
# # all_comments = submissions.comments.list()

# for title, text in top2: 
#     print (title, text)

# topics_dict = { "title":[], \
#     "score":[],\
#         "id":[], "url":[],\
#             "comms_num": [], \
#                 "created": [], \
#                     "body":[]}


# for submission in submissions:
#     topics_dict["title"].append(submission.title)
#     topics_dict["score"].append(submission.score)
#     topics_dict["id"].append(submission.id)
#     topics_dict["url"].append(submission.url)
#     topics_dict["comms_num"].append(submission.num_comments)
#     topics_dict["created"].append(submission.created)
#     topics_dict["body"].append(submission.selftext)


# pd = pandas
# topics_data = pd.DataFrame(topics_dict)

# print(topics_data)


# # sentence = VG_dict
# # score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# # print(score)