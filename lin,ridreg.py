# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:26:27 2020

@author: saisr
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

from sklearn.datasets import load_boston
boston_s = load_boston()
print(boston_s)

boston_data = pd.DataFrame(boston_s.data,columns = boston_s.feature_names)
print(boston_data.head(20))

boston_data["LandPrice"] = boston_s.target

NewX = boston_data.drop("LandPrice",axis = 1)
NewY = boston_data["LandPrice"]
print(NewX) 
print(NewY)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(NewX,NewY,test_size = 0.3 , random_state = 1)
lin = LinearRegression()
lin.fit(X_train,Y_train)

rr = Ridge(alpha = 0.01,solver = "cholesky")  #the smaller the value of alpha the 
                                               #higher would be the magnitude of coefficients
rr.fit(X_train,Y_train)

train_score = lin.score(X_train,Y_train)
test_score = lin.score(X_test,Y_test)

ridge_train_score = rr.score(X_train,Y_train)
ridge_test_score = rr.score(X_test,Y_test)

print("In linear regression training and test scores :",train_score,test_score)
print("in ridge regression traning and test scores are :",ridge_train_score,ridge_test_score)


plt.plot(rr.coef_,marker = '*',markersize = 5,color = "red",label = r'Ridge;$\alpha = 0.01$')
plt.plot(lin.coef_,marker = '+',markersize= 15,color = "blue",label = "Linear Regression")
plt.xlabel("Coeffienct Index",fontsize = 14)
plt.ylabel("Coefficient magnitude",fontsize = 16)
plt.legend(loc = "best")
plt.show()


boston_dataset = load_boston()

print(boston_dataset)

boston = pd.DataFrame(boston_dataset.data,columns = boston_dataset.feature_names)
print(boston)

boston["MEDV"] = boston_dataset.target

correlation_matrix = boston.corr().round(2)
print(correlation_matrix)

import seaborn as sns
sns.set(rc ={'figure.figsize':(12,10)})
sns.heatmap(data = correlation_matrix,annot = True)
plt.show()


X = pd.DataFrame(np.c_[boston['LSTAT'],boston['RM']],columns = boston['LSTAT','RM'])
print(X)
Y= boston['MEDV']
print(Y)



















