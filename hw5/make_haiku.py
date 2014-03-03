# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:32:02 2014

@author: dmichael
"""
from random import *
from testFacebook import *
from num_syllables import *

def sort_by_syllable(syll_dict,tweetsraw):
    '''this takes a list of strings and outputs a dictionary of lists of words
    with the same number of sylables'''
    tweets0=[]    
    tweets1=[]
    tweets2=[]
    tweets3=[]
    tweets4=[]    
    
    for i in range(len(tweetsraw)):        
        if get_num_syllables(syll_dict,tweetsraw[i]) == 1:
            tweets1.append(tweetsraw[i])
        elif get_num_syllables(syll_dict,tweetsraw[i]) == 2:
            tweets2.append(tweetsraw[i])
        elif get_num_syllables(syll_dict,tweetsraw[i]) == 3:
            tweets3.append(tweetsraw[i])
        elif get_num_syllables(syll_dict,tweetsraw[i]) == 4:
            tweets4.append(tweetsraw[i])
        elif get_num_syllables(syll_dict,tweetsraw[i]) == 0:
            tweets0.append(tweetsraw[i])
    tweets = {1:tweets1,2:tweets2,3:tweets3,4:tweets4}
    print tweets
    return tweets
    
def build_haiku(depth,tweets):
    '''this takes the number of syllables in a line and the output of sort_by_syllables
    and outputs a nested list of strings that has the number of sylables as the imput'''
    if depth==1:
        end = tweets[1]
        haiku = end[randint(1,len(end)-1)]
        return haiku
        
    if depth > 1:
        if depth > 4:
            y=randint(1,4)
        elif depth <= 4:
            y = randint(1,depth)    
        x = build_haiku(depth-y,tweets)        
        notend = tweets[y]
        
        count = 0
        while len(notend) == 0:
            if count < 20:            
                y = randint(1,4)
                notend = tweets[y]
            else:
                return "Insufficient Posts!"
            count += 1
            
        if not type(x) == type(None):
            haiku = [notend[randint(0,len(notend)-1)]]
            haiku.append(x)
        else:
            haiku = flatten([notend[randint(0,len(notend)-1)]])
        return haiku

def flatten(test_list):
    '''this takes a list of lists and outputs a list'''
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first, rest = test_list[0], test_list[1:]
        return flatten(first) + flatten(rest)
    else:
        return [test_list]
        
def print_haiku(syll_dict,name):
    '''this prints a haiku from syllable dictionary and username'''
    tweetsraw = get_words(name)
    print tweetsraw
    tweets = sort_by_syllable(syll_dict,tweetsraw)
    line1 = build_haiku(5,tweets)
    line2 = build_haiku(7,tweets)
    line3 = build_haiku(5,tweets)
    a = (flatten(line1))
    b = (flatten(line2))
    c = (flatten(line3))
    print ' '.join(a)
    print ' '.join(b)
    print ' '.join(c)