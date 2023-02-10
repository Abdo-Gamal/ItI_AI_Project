
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

def make_Dataframe(email_form_original_dataset,is_spam,tokens):
   for i,email in enumerate(email_form_original_dataset["text"]):
      row=[]
      for word in future:
        if word in str(email): 
         row.append(tokens.count(word))
        else:row.append(0)
      row.append(is_spam)
      data.append(row)
   return data


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

frq_hame_future=sorted(frq_hame_future, key=lambda x:x[0],reverse=True)
frq_spam_future=sorted(frq_spam_future, key=lambda x:x[0],reverse=True)

frq_hame_future=frq_hame_future[1:6]
frq_spam_future=frq_spam_future[1:6]
print(frq_spam_future)
future=[]
for item in frq_hame_future:
   future.append(item[1])
for item in frq_spam_future:
   future.append(item[1])
future.extend(["is_spam"])
print(future)
#                                                make future 
data=[[]]
make_Dataframe(ham_email_form_original_dataset,0,hame_tokens)
make_Dataframe(spam_email_form_original_dataset,1,spam_tokens)
transform_futue_to_dataframe =pd.DataFrame( data,columns=future)
print(transform_futue_to_dataframe)
#                                                make future 



