from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd
import string
#                                            preprocess section
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

#                                            future extraction section
#                                            future extraction section

#                                              uniqe function 
def Uniqe(sequence):
    seen=set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

#                                              uniqe function 
def vectorize(tokens):
    vect=[]
    for w in filter_vocab:
      vect.append(tokens.count(w))
    return vect
#                                              use vectorize and Uniqe
stop_words1=[':',';','?',',','.','!']#stop_words can get form nltk
spcial_char1=[':',';','?',',','.','!']#spcial_char can get from str.panctuation
string1="Welcom to Greate leaning ,now start leaning to great welcom "
string2="leaning is good practice"

string1=string1.lower()
string2=string2.lower()

tokens1=string1.split()
tokens2=string2.split()
print(tokens1)
print(tokens2)

vocab=Uniqe( tokens1+tokens2)
print(vocab)

filter_vocab=[]

for w in vocab:
    if w not in stop_words1 and w not in spcial_char1:
       filter_vocab.append(w)

print(filter_vocab)
vector1=vectorize(tokens1)
print(vector1)
vector2=vectorize(tokens2)

print(vector2)