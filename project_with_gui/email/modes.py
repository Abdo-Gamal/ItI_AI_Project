import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import *



def split_Data():
    path=select()
    dataset=pd.read_csv('path')
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


def KNN(my_list):
     from sklearn.neighbors import KNeighborsClassifier
     Knn = KNeighborsClassifier(n_neighbors=2)
     Knn.fit( my_list[0],my_list[2])
     pred = Knn.predict(my_list[1])
     return pred

def naive_bayes(list):
     from sklearn.naive_bayes import GaussianNB
     nBmodel = GaussianNB()
     nBmodel.fit(list[0],list[2])
     y_predicted = nBmodel.predict(list[1])
     return y_predicted

def Accuracy(list,y_predict):
     from sklearn.metrics import accuracy_score
     acc=accuracy_score(list[3],y_predict)
     print(acc)
     return acc

def Confusion(list,y_predict):
     from sklearn.metrics import confusion_matrix
     x=pd.DataFrame(
        confusion_matrix(list[3],y_predict),
        columns=['predicted Not spam', 'predicted spam'],
        index=['Actual Not spam', 'Actual spam']
        )
     print(x)
     return x

def showHistogram(acc):
    plt.hist([acc])
    plt.show()
# var1 var2
def mainfun(sel_mode,sel_con_Or_acc):
     print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
     # list_of_acc=[]
     my_list=split_Data()
     pred=[]
     if sel_mode ==1 :                        #knn
          pred=KNN(my_list)
          acc=Accuracy(my_list,pred)
     if sel_mode == 2:                       #naive_bayes
          pred=naive_bayes(my_list)
          acc=Accuracy(my_list,pred)
     if sel_mode==2:
        pred=DecisionTree(my_list)
        acc=Accuracy(my_list,pred)


     #####################################
     if sel_con_Or_acc==1:                    #accurcy
        showHistogram(acc)
     if sel_con_Or_acc==2:                  #cinfsion
        con=Confusion(my_list,pred) 
        showHistogram(list(con))


mainfun(var1,var2)