# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:59:03 2020

@author: saisr
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns

data = pd.read_csv("titanic.csv")
print(data.head())

titanic = pd.DataFrame(data)
print(titanic)
print("tot no. of passenger:"+str(len(titanic)))

sns.countplot(data = titanic,hue = "Pclass",x = "Survived")
plt.show()


titanic["Pclass"].plot.hist()
plt.show()

titanic.info()

sns.boxplot(x = "Sex",y = "Age",data = titanic)
plt.show()

titanic.drop(["Name","Ticket","Cabin","PassengerId"],axis =1 ,inplace = True)
titanic["Age"].fillna((titanic["Age"].mean()),inplace = True)

sex= pd.get_dummies(titanic['Sex'],drop_first = True)
Pls = pd.get_dummies(titanic['Pclass'])
embark = pd.get_dummies(titanic['Embarked'],drop_first = True)

titanic.drop(['Sex','Pclass','Embarked'],axis =1,inplace = True)

titanic = pd.concat([titanic,sex,Pls,embark],axis = 1 )
titanic.head()

X = titanic.drop(["Survived"],axis = 1)
y = titanic["Survived"]
print(X)
print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state =1 )

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)
print(predictions)

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
print(confusion_matrix(y_test,logmodel.predict(X_test)))
print(classification_report(y_test,logmodel.predict(X_test)))
print(accuracy_score(y_test,logmodel.predict(X_test)))
































