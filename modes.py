import pandas as pd
import numpy as np


dataset=pd.read_csv('myfuturesfile.csv')

def split_Data(data):
   x=pd.DataFrame(dataset.iloc[:,:-1])
   y=pd.DataFrame(dataset.iloc[:,-1])
   
   from sklearn.model_selection import train_test_split
  
   x_train , x_test , y_train , y_test = train_test_split(x,y,random_state=1)
   l=[x_train , x_test , y_train , y_test ]
   return l

def DecisionTree(list):   
      from sklearn import tree
      model = tree.DecisionTreeClassifier()
      model.fit(list[0],list[2])
      y_predict = model.predict(list[1])
      return y_predict


def KNN(list):

     from sklearn.neighbors import KNeighborsClassifier
     Knn = KNeighborsClassifier(n_neighbors=1)
     Knn.fit(list[0],list[2])
     pred = Knn.predict(list[1])
     return pred

def naive_bayes(list):
     from sklearn.naive_bayes import GaussianNB
     nBmodel = GaussianNB()
     nBmodel.fit(list[0],list[2])
     y_predicted = nBmodel.predict(list[1])
     return y_predicted

def Accuracy(list,y_predict):
     from sklearn.metrics import accuracy_score
     print(accuracy_score(list[3],y_predict))

def Confusion(list,y_predict):
     from sklearn.metrics import confusion_matrix
     print(pd.DataFrame(
        confusion_matrix(list[3],y_predict),
        columns=['predicted Not spam', 'predicted spam'],
        index=['Actual Not spam', 'Actual spam']
        ))

def mainfun():
   pass 
   