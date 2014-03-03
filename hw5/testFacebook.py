# -*- coding: utf-8 -*-
# Bonnie Ishiguro
"""
Created on Thu Feb 27 20:12:00 2014

@author: bishiguro
"""
from num_syllables import *
from pattern.web import Facebook, FRIENDS, NEWS
token = "CAAEuAis8fUgBAC3MHxZAMvEy9Q4uveZB9AVJc11AKo5sK4yJVIy0PitOYNZAhRBkCjXcvT2uaCgPuElZBMEeZBLcRtiopFh4bnraCPjC3iZBb8wfRG2cBLaiIVyuj4xH7ZBFZAjyWZCmZB3yEtY11uDJyvRlW12oKjkN286eYP4R6rYTgLT8v2MtdJlHrwq5AuAW8ZD"
fb = Facebook(license = token)
me = fb.profile(id=None)

def get_posts(name): 
    '''returns a list of a user's recent posts'''
    posts = []
    friend_name = ""
    friend_news = ""
    my_friends = fb.search(me[0],type=FRIENDS,count=1000)
    for friend in my_friends:
        if name == str(friend.author[1]):
            friend_name = str(friend.author[1])
            friend_news = fb.search(friend.id,type=NEWS,count=1000)
    if not(friend_name == ""):
        for news in friend_news:             
            if (news.author[1]) == friend_name:
                if not("friends" in str(news.text)) and not("likes" in str(news.text)) and not("event" in str(news.text)) and not("post" in str(news.text)) and not("photo" in str(news.text)) and not("link" in str(news.text)) and not("profile" in str(news.text)) and not("invited" in str(news.text)) and not("status" in str(news.text)) and not("timeline" in str(news.text)) and not("tagged" in str(news.text)) and not("changed" in str(news.text)):   
                    posts.append(str(news.text))
        return posts
    return ""
    
def get_words(name): 
    '''returns all words used by the user in recent posts'''
    import re
    all_words = []
    if get_posts(name) == "":
        raise Exception("This account doesn't exist.")
    else:
        all_posts = get_posts(name)
        for post in all_posts:
            words_in_post = re.findall("[\w'-\*\"\']+",post) 
            for word in words_in_post:          
                all_words.append(word)
    if len(all_words) < 15:
        raise Exception("Not Enough Words")
    else:
        return all_words