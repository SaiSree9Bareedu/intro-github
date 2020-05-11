# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:05:09 2020

@author: saisr
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Advertising.csv")
print(data.head(10))


s = data.drop("Unnamed: 0",axis = 1 , inplace = False)
                                                          
                                                         
                                                        
                                                         
print(s.head(10))

X = s["TV"].values
print(X)
Y = s["sales"].values
print(Y)



mean_x = np.mean(X)
print(mean_x)
mean_y = np.mean(Y)
print(mean_y)

#to find m and c values for y = mx +c ,we use ordinary least 
#squares formula summation[(x-xmean)*(y-ymean)]/summation[sqaure(x-xmean)]

n = len(X)
numer = 0
denom= 0
for i in range(n):
    numer += (X[i]-mean_x)*(Y[i]-mean_y)
    denom += (X[i]-mean_x)**2
m = numer/denom
c = mean_y -(m*mean_x)
print(m)
print(c)

print("The linear equation is Y=: {:.2}+{:.3}X".format(c,m))

#plotting regression line with the possible x and y values 
#nothing but our outputs ,with the input X,Y as the values in 
#the form of scatter plot to check how far the otput values 
#regression line best fits the input values X;Y in the form of catter plt
min_x = np.min(X)+100
max_x = np.max(X)-100


#we take min and max values of X as interval and +100 and -100 
#so that x values lies inside the interval in any case

x = np.linspace(min_x,max_x,1000)
y = m*x+c 

#plotting regessrion line with x,y values
plt.plot(x,y,color = 'red', label ="Regressionline")
plt.scatter(X,Y,color = 'Blue' , label = "Scatterplot")
plt.xlabel("expenditure on TVs")
plt.ylabel("TVs sold-sales")
plt.legend(loc = "best")
plt.show()


y_pred = c+m*X[1]
print(y_pred)
print(Y[1])

#calculation Rsquare -coefficient of determnation value

ss_tot = 0
ss_res = 0
for i in range(n):
    y_pred = c + m*X[i]
    ss_tot += (Y[i]-mean_y)**2
    ss_res += (Y[i]-y_pred)**2
r2 = 1 - ss_res/ss_tot
print("R2 score")
print(r2)



from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

m = 160
X = 6*np.random.rand(m,1)
y = 1.5*X**2+X+2+np.random.randn(m,1)

print(X[0])

plt.plot(X,y,'.')
plt.show()

#now as we cant fit a line or a single degree linear equation into these points we requrie a curve to pass through , hence a polynorminal expression of more than 1 degree or degree 2 can pass through the points as acurve

poly_features = PolynomialFeatures(degree =2,include_bias =False) #step1 - Calling function

#by default bias remains true which means all the polynominal features are 0 but we need polynomial here so we mark bias as false
X_ploy = poly_features.fit_transform(X)

#step2 -assign polynomial features to variable X_ploy and use fit_tranform

print(X_ploy[0])
#X_poly contains both oroginal feature and extended polynomiak feature in X. now we can fit our linear regression model to this extended training data
#hence import linear regression class from linear model moduel

lin_reg = LinearRegression()


lin_reg.fit(X_ploy,y)
lin_reg.intercept_,lin_reg.coef_
plt.scatter(X,y,label = "Inputdata",color = "blue")
plt.plot(X,lin_reg.predict(X_ploy),'.',color = "r",label = "Predictions")
plt.legend(loc = "best")
plt.show()

#fitting polynomial regression to the above data set after giving X and y values

X = s.iloc[:,0:3]
y = s.iloc[:,3:]

lin = LinearRegression()
lin.fit(X,y)

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)
poly.fit(X_poly,y)

lin2 = LinearRegression()
lin2.fit(X_poly,y)

print(lin.coef_)
print(lin.intercept_)

g = lin2.predict(poly.fit_transform([[151.5,41.3,58.5]]))
print(g)



















