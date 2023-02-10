from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd
import string

#                                            preprocess section

#                                         functions to remove punctuation from dataset
PUNCT_TO_REMOVE=string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('','',PUNCT_TO_REMOVE))

text="I'm have alote of  punctuation !!. all special chracter will be removed ;;..so # :(  :( " 
# print(remove_punctuation(text))

#                                            functions to remove stopwords  from dataset  "edit"

STOPWORDS=stopwords.words("english")  #  stopword like " an a the in  as  ...."
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

text2="my name is  abdo  \nI will git my PH and master from anerica in as the a an be  "
# print(remove_stopwords(text2))

#                                            functions to  stem words 
stemer=PorterStemmer()

def stem_words(text):
    return " ".join([stemer.stem(world) for world in text.split()])

text3="I am loving to player games . I liked gaming very mach . one of my favorite games"
# print(stem_words(text3))

#                                            functions to  deEmoje
def DeEmojify(text):
    return text.encode("ascii","ignore").decode("ascii")
text4="📙 Emojipedia — 😃 Home of Emoji Meanings 💁👌🎍😍"
# print(DeEmojify(text4))
