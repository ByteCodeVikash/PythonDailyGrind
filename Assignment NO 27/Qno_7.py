"""
7.Create a function that accepts a long text string, splits it into words, and uses the filter()
and map() functions to strip out punctuation and convert all words to lowercase. Return
a set of unique valid words.
"""

import string

def func(text):

    raw_word=text.split()

    clean_map=map(lambda w:w.strip(string.punctuation).lower(),raw_word)
    
    valid_word=filter(None,clean_map)

    unique_word=set(valid_word)

    return unique_word

text="this is long text string"
print(func(text))    	



