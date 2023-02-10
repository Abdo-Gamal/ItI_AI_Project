from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd
import string
import FutureExtraction as fe
import PreprocessPhase as pp

#                                                 read data set 
origin_data_set=pd.read_csv("emails.csv")
# print(origin_data_set)
dataset_as_string=[]
for i,line in enumerate(origin_data_set["text"]): #transulte datafrom text  to one string
   dataset_as_string.append(str(line))

# print(dataset_as_string)

#                                                prepareDataSet
dataset_as_string=fe.remove_punctuation(dataset_as_string)
print(dataset_as_string)

