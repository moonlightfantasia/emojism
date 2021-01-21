"""Emojism core function"""

#Project: Emojism
#Author: Littin Rajan


#importing required libraries
import json
import re

#load dictionary
def load_dictionaries():
    with open(r'emojism/resources/emoji.json') as emoji_json_file:
        emoji_data = json.load(emoji_json_file)
    with open(r'emojism/resources/emoticon.json') as emoticon_json_file:
        emoticon_data = json.load(emoticon_json_file)
    #return emoji and emoticon dictionaries
    return emoji_data,emoticon_data

#load emoji and emoticon dictionaries
EMOJI_DICT,EMOTICON_DICT = load_dictionaries()

#define emoji and emoticon pattern
EMOJI_PATTERN = u'(' + u'|'.join(re.escape(u) for u in EMOJI_DICT) + u')'
EMOTICON_PATTERN = u'(' + u'|'.join(k for k in EMOTICON_DICT) + u')'


#function to remove emoji and emoticons
def emo_eraser(text):
    text = re.sub(EMOJI_PATTERN, "", str(text))
    text = re.sub(EMOTICON_PATTERN, "", str(text))
    text = re.sub(" {2,}", " ", str(text))
    return text
    
    
#function to remove emoji and emoticons
def emo_count(text,mode="all"):
    em_list = re.findall(EMOJI_PATTERN, str(text))
    if mode=="unique" and em_list:
        em_count = len(set(em_list))
    elif mode=="all" and em_list:
        em_count = len(em_list)
    else:
        em_count = 0
    return em_count
    
    
#function to get all emoji
def emo_get(text):
    try:
        em_pat = [x for x in re.findall(EMOJI_PATTERN, str(text)) if x]
        if em_pat!=0:
            em_all = ','.join(re.findall(f"[{''.join(em_pat)}]", str(text)))
        else:
            em_all = None
    except Exception:
        em_all = None
    return em_all
    
    
#function to get help
def helpme():
    print("""
    Emojism is a simple package for handling emoji and emoticons
    
    Author: Littin Rajan
    
    Modules: 
            #emo_eraser(<input text>)
            For removing all Emoji and Emoticons from text
            
            #emo_count(<input text>)
            For counting Emoji occurences in a text
            Having two modes "unique" and "all"
            emo_count(<input text>, mode="all")  will return the whole count. mode="all" is the default values
            emo_count(<input text>, mode="unique")  will return only the unique count of Emoji
            
            #emo_get(<input text>)
            For collecting all Emoji present in the input text. Return all emoji as a coma seperated string.
            
    ----------------------------------------------Enjoy Emojism---------------------------------------------
    """)