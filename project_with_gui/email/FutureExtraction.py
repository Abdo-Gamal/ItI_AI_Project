from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd
import string

#                                              uniqe function 
def Uniqe(sequence):
    seen=set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

#                                              uniqe function 
def vectorize(tokens,filter_vocab): # count number of filter words in all data set 
    req=[]
    for w in filter_vocab:         #filter_vocab is my future 
      req.append(tokens.count(w)) # tokens is all dataset or all words 
    return req
#                                              
