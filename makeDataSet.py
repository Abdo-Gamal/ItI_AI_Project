from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd
import string
import FutureExtraction as fe
import PreprocessPhase as pp

def stransulate_DF_to_string( input):
   dataset_as_string=""
   for i,line in enumerate(origin_data_set["text"]): #transulte datafrom text  to one string
      dataset_as_string+=str(line)
   return dataset_as_string

origin_data_set=pd.read_csv("emails.csv")# read data set 
dataset_as_string=""
dataset_as_string=stransulate_DF_to_string(origin_data_set)
# print(f"dataset_as_string = {dataset_as_string}")
# print("\n")
# print("\n")
#                                                prepareDataSet
dataset_as_string=dataset_as_string.lower()
dataset_as_string=pp.remove_punctuation(dataset_as_string)
dataset_as_string=pp.remove_stopwords(dataset_as_string)
dataset_as_string=pp.stem_words(dataset_as_string)
dataset_as_string =pp.DeEmojify(dataset_as_string)
# print(dataset_as_string)
#                                                extract futures from dataset
tokens=dataset_as_string.split()
# print(f" tokens = {tokens}")
vocab=fe.Uniqe( tokens)
# print(f" vocab = {vocab}")
future=fe.vectorize(tokens)
print(f" future = {future}")


