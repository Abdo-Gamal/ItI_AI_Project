from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd
import string

#                                         functions to remove punctuation from dataset
PUNCT_TO_REMOVE=string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('','',PUNCT_TO_REMOVE))

#                                            functions to remove stopwords  from dataset  "edit"

STOPWORDS=stopwords.words("english")  #  stopword like " an a the in  as  ...."
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

#                                            functions to  stem words 
stemer=PorterStemmer()

def stem_words(text):
    return " ".join([stemer.stem(world) for world in text.split()])

#                                            functions to  deEmoje
def DeEmojify(text):
    return text.encode("ascii","ignore").decode("ascii")

