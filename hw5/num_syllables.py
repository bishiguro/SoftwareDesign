# Bonnie Ishiguro

from pattern.web import *
import pickle

word_to_syllables = pickle.load(open("save.p","rb"))

def gen_syllable_dict(): # generate syllable dictionary
    '''this takes Webster's dictionary and generates a
    syllable dictionary'''
    d = {}
    parts = ['n.', 'v.', 'adv.', 'a.','prep.'] # part of speech - to identify line with the syllabic word
    with open('Websters.txt', 'rb') as f:
        current_word = ""
        for row in f: # for each row in Webster's
                words = row.split()
                if len(words) == 1 and words[0].isupper(): # check if the row contains a Webster's entry
                    current_word = words[0]
                if "Etym." in words or True in [p in words for p in parts]: # check if the following row contains the syllabic word                   
                    d[current_word] = word_to_syllable(words[0].strip(',')) # save the word and its syllabic word in the syllable dictionary
                    #print "saving word: ",current_word
    pickle.dump(d,open("save.p","wb")) # save the syllable dictionary in the file save.p
    
def word_to_syllable(word): 
    '''generates syllabic word for a dictionary entry'''    
    syllSeparators = ["*","\"","\'","`","-"] # number of syllables determined by number of sections separated by punctuation mark
    num_sylls = 1 # no punctuation marks = 1 syllable
    for i in range(len(word)):
        for j in syllSeparators:
            if (word[i] == j) and (i != len(word)-1):      
                num_sylls += 1
    return num_sylls

def get_num_syllables(syll_dict, word): 
    '''this takes a string as an imput and outputs an int 
    coresponding to te number of syllables in the word'''
    if word.upper() in syll_dict:     
        return syll_dict[word.upper()] # if in syllable dictionary, return number of syllables 
    return 0 # not in Webster's dictionary