
from library import * 

def stransulate_DF_to_string( input):
   dataset_as_string=""
   for i,line in enumerate(origin_data_set["text"]): #transulte datafrom text  to one string
      dataset_as_string+=str(line)
   return dataset_as_string

def prepareDataSet(string_dataset):
   string_dataset=string_dataset.lower()
   string_dataset=pp.remove_punctuation(string_dataset)
   string_dataset=pp.remove_stopwords(string_dataset)
   string_dataset=pp.stem_words(string_dataset)
   string_dataset =pp.DeEmojify(string_dataset)
   return string_dataset.split()

def make_future(email_form_original_dataset,is_spam):
   for i,email in enumerate(email_form_original_dataset["text"]):
      row=[]
      for word in future:
        if word in email: 
         row.append(hame_tokens.count(word))
        else:row.append(0)
      row.append(is_spam)
      transform_futue_to_dataframe[len(transform_futue_to_dataframe)]=row


origin_data_set=pd.read_csv("emails.csv")# read data set 
ham_email_form_original_dataset=origin_data_set[origin_data_set.spam==0]
spam_email_form_original_dataset=origin_data_set[origin_data_set.spam==1]

ham_email_form_original_dataset_as_string=stransulate_DF_to_string(ham_email_form_original_dataset)
spam_email_form_original_dataset_as_string=stransulate_DF_to_string(spam_email_form_original_dataset)

hame_tokens=prepareDataSet(ham_email_form_original_dataset_as_string)
spam_tokens=prepareDataSet(spam_email_form_original_dataset_as_string)
# print(spam_tokens)

#                                                extract futures from dataset
hame_future=fe.Uniqe(hame_tokens)
spam_future=fe.Uniqe(hame_tokens)
frq_hame_future=[[hame_tokens.count(words), words ] for words in hame_future]
frq_spam_future=[[hame_tokens.count(words), words ] for words in hame_future]

frq_hame_future=sorted(frq_hame_future, key=lambda x:x[0])
frq_spam_future=sorted(frq_spam_future, key=lambda x:x[0])
print(frq_spam_future)
frq_hame_future=frq_hame_future[:5]
frq_spam_future=frq_spam_future[:5]
future=frq_hame_future
future=future.extend(frq_spam_future)
future.append("Is_spam")
#                                                make future 
transform_futue_to_dataframe =pd.DataFrame(columns=future)
make_future(ham_email_form_original_dataset,0)
make_future(spam_email_form_original_dataset,1)
print(transform_futue_to_dataframe.iloc)



