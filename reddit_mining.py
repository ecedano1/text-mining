import praw
import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#used for measuring the intensity of the natural language of humans 


reddit = praw.Reddit(client_id='1RjIws9QcWKMww',
                    client_secret='-K-88s47llEE3_1FASt-ey_UHZ4',
                    username='ecedano1',
                    password='ECedano11!',
                    user_agent= 'windows:com.pythonsentimentapp.myredditapp:v1.2.3 (by/u/ecedano1)')

sub = 'modernwarfare' #becomes the variable for the subreddit that will be used to pull the submissions/comments from
submissions = reddit.subreddit(sub).new(limit=15)


#Testing features of the submission functions
# (limit = 20)
# top('day', limit = 5) other functions 
# hot('day', limit = 2)
# new(limit= 3)

for submission in submissions:
    """
    Using this to pull the most recent comments an their respective titles and bodies. 
    Helped me pinpoint which comments to use for sentiment analysis.
    
    """
    print(submission.author, submission.title, submission.selftext, '\n')


########################################### FINAL ATTEMPT #############################################


def sentiment_scores(sentence): 

    # Create a SentimentIntensityAnalyzer object. 
    sia_obj = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # object gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sia_obj.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    print("Sentence Overall Rated As", end = " ") 
  

    """decide sentiment as positive, negative and neutral based on the compounded scores of each sentence used."""

    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral") 


# vg_comment1= 'reddit_comment.txt' : DOES NOT analyze it properly and give 100% neutral each time .TXT File is used


if __name__ == "__main__" : 
  
    print("\n1st comment :") 
    sentence = 'Everyone constantly bitches and moans that each new COD is a re-skin of the last.\
        The most innovative COD in a minute drops, and now people just want a re-skin of Black Ops 4.\
            Hopefully Infinity Ward can distinguish in this clown show the legitimate criticism from the people who just spend their entire day bitching on this website just to bitch.\
                Great game IW. Definitely needs some tweaks like any game that just came out, but this is one of the best COD games yet.'
    sentiment_scores(sentence)
    
    #it would not judge the text file appropiately so I used this method instead. 
    #Author: whatschildsupport

    # function calling  
  
    print("\n2nd comment :") 
    sentence = 'Here\'s an analogy for all of you "tactical" players.\
        Imagine you\'re in a math class, and it\'s a breeze for you but everyone else is struggling, even though they\'re using a calculator.\
            You finish all the tests 3x faster than anyone else and you get high scores, all without using a calculator.\
                The teacher doesn\'t make you come to class on Fridays, because you\'re doing so well you deserve to get rewarded.\
                    Then next year you get a teacher who requires you to show your work.\
                         He thinks the other students are getting upset because you\'re finishing so much faster than they are.\
                             He wants to make sure they don\'t drop the class. You\'ve never needed to show your work in the past, and while you know how to do that, you\'ve never had to waste your time with it before.\
                                You were smart enough to do it all in your head. Now you\'re only finishing your tests a few minutes ahead of everyone.\
                                    Still doing well but not fast enough to get significantly rewarded for it. Your intelligence isn\'t lacking, it\'s the rules holding you back from showing your full capabilities.\
                                        This is what it\'s like going from Infinity Ward\'s last CoD to this one. The maximum speed at which you can do things in this CoD is so god damn slow that the skill gap is almost nonexistent.\
                                            No one finds camping impressive, because it\'s easy as shit. We all know how to do it. You shouldn\'t feel like you\'re some genius who came up with the strategy.\
                                                It\'s literally what 99 percent of people do when they get their first CoD. Congrats on not getting better after your first month of playing.'
    sentiment_scores(sentence) 
  
    print("\n3rd comment :") 
    sentence = 'Ive played every call of duty since COD4. I must say of all aspects of the game their is not alot that is good in my opinion.\
        The guns are mediocre, the maps are probably the worst thing in this game right now, Too many weapon mods/attachments.\
            The movement is okay i guess. Anyone thats saying this game is bad when their are not doing good in multiplayer i can understand.\
                I guarantee in 2 months no one will want too play public matches cause it is not fun at all'
    sentiment_scores(sentence) 


    print("\n4th comment :")
    sentence4 = 'What really needs to happen in Call of Duty: Modern Warfare I\'m going to speak more with reason, than blind rage, or a blind fanboy opinion.\
        The game\'s core is solid, everything feels smooth and polished. Gun balancing needs worked. But there\'s a foundation here that can still be salvaged.\
            It\'s the idiotic map design IW decided to go with.\
                And I\'m not going to jump on the "bring 3-lane maps back" bandwagon that all these YouTubers, and their brainwashed fans are pining over.'
    sentiment_scores(sentence)
    #author: GravelIsNotAFood

    print("\n5th comment :")
    sentence5 = 'I feel like there hasn\'t been enough of a fuss about this, but where are all the gamemodes?!\
        Maps and playstyles aside, this is my biggest issue with the game.\
            This is the least 6v6 content I\'ve ever seen in a COD. I fully understand that people want more from COD than just 6v6, but it feels so neglected.\
                Only 5 traditional gamemodes, only 6 proper maps, I\'ve played betas with more replay value than this.\
                    I can\'t help but feel like Infinity Ward tried too hard to please everyone and ended up not fully satisfying anyone.\
                        Any other COD game would\'ve been crucified for only having 5 gamemodes at launch.\
                            Where\'s Hardpoint, CTF, Demolition, something like Control out of BO4? Please Infinity Ward, can we have some more gamemodes to keep the game somewhat fresh until new maps arrive?\
                                I\'m already getting bored with this game.'
    sentiment_scores(sentence5)
     #author: RedDevilLuca





############################# DIFFERENT ATTEMPT #2 ################################################
# import json


# def vg_comment1 (): 
#     filename1 = 'reddit_comment.txt'
#     reddit_comment1 = {}

#     with open(filename1) as rc1:
#         for line in rc1:
#             comment, description = line.strip().split(' ', 1)
#             reddit_comment1[comment] = description.strip()

# # print(json.dumps(reddit_comment1))

# print (vg_comment1)
# print(type(vg_comment1))

#############################  DIFFERENT ATTEMPT #3 #########################################

# VG_comment= dict('reddit_comment.txt')

# vg_comment1= reddit.submission(id = 'dphxoh')
# vg_comment2= reddit.submission(id = 'dphxzy')
# vg_comment3= reddit.submission(id = 'dphxif')
# vg_comment4= reddit.submission(id = 'dphya6')
# vg_comment5= reddit.submission(id = 'dphycw')

# sentence1 = vg_comment1
# sentence2= vg_comment2
# sentence3= vg_comment3
# sentence4 = vg_comment4
# sentence5= vg_comment5

# score1 = SentimentIntensityAnalyzer().polarity_scores(vg_comment1)
# score2 = SentimentIntensityAnalyzer().polarity_scores(sentence2)
# score3 = SentimentIntensityAnalyzer().polarity_scores(sentence3)
# score4 = SentimentIntensityAnalyzer().polarity_scores(sentence4)
# score5 = SentimentIntensityAnalyzer().polarity_scores(sentence5)

# print(score1)
# print(score2)
# print(score3)
# print(score4)
# print(score5)

# ######################### FOR REDDIT POSTING visualisation: FAIL lol - didn't work ##################################

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