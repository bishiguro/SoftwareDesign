# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 22:33:27 2014

@author: bishiguro
"""

from num_syllables import *
from make_haiku import *

def setup():
    '''this resets after edits are made'''
    gen_syllable_dict()
    word_to_syllables = pickle.load(open("save.p","rb"))

def genHaiku():
    '''this generates a haiku'''
    friend = raw_input("Enter the Name of a Facebook Friend: ")
    print_haiku(word_to_syllables,friend)
