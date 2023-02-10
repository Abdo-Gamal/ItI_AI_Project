from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd
import string

#                                            future extraction section

#                                              uniqe function 
def Uniqe(sequence):
    seen=set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

#                                              uniqe function 
def vectorize(tokens): # count number of filter words in all data set 
    vect=[]
    for w in filter_vocab:         #filter_vocab is my future filter_vocab
      vect.append(tokens.count(w)) # tokens is all dataset or all words 
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
# print(f" tokens1 = {tokens1}")
# print(f" tokens2 = {tokens2}\n")

vocab=Uniqe( tokens1+tokens2)
# print(f" vecab= {vocab}")

filter_vocab=[]

for w in vocab:
    if w not in stop_words1 and w not in spcial_char1:
       filter_vocab.append(w)

# print(f"filter_voca ={ filter_vocab}\n")
# vector1=vectorize(tokens1)
# print(vector1)
# vector2=vectorize(tokens2)

# print(vector2)