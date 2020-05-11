# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:57:10 2020

@author: saisr
"""

#scaling data by MinMaxScaler and StandardScaler

#normalizing categorical features
import numpy as np
import pandas as pd
from sklearn import preprocessing
data = { "price": [23,4,6,7,89,245]}
print(data)

s = pd.DataFrame(data)
print(s)

min_max_normalizer = preprocessing.MinMaxScaler()
print(min_max_normalizer) #min vale 0, max value 1
scaled_data = min_max_normalizer.fit_transform(s)
print(scaled_data)
d = pd.DataFrame(scaled_data)
print(d)

#Z Score normalization based on mean and variance of a data
#after normalizing- mean 0 , vari 1
#preferred when our data has more outliers we can take it as preprocessing method

f = pd.DataFrame(data)
print(f)

min_max_normalizer = preprocessing.scale(f)
print(min_max_normalizer)
a = pd.DataFrame(min_max_normalizer , columns = ['price'])
print(a)

#standard scalar- features inthe data is standardized by removing mean and reducing to unit variance, 
#the standard score of sample is (x-mue)/sigma

from sklearn.preprocessing import StandardScaler
data_ = np.array([[0,0],[0,0],[1,1],[1,1]])

scaler = StandardScaler()
print(scaler.fit(data_))

print(scaler.mean_)
print(scaler.transform(data_))

#converting categorical variable to numerical


#if we want to reverse this encoding that is to get back words from encoded numercials
#First Feature
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy',
           'Sunny','Overcast','Overcast','Rainy']
#second Feature
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild',
       'Hot','Mild']
#Label or target variable
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
weather_encoded = le.fit_transform(weather)
print(weather_encoded)

label = le.fit_transform(play)
print(label)

temp_encoded = le.fit_transform(temp)
print(temp_encoded)

#if we want to reverse this encoding that is to get back words from encoded numercials

temp = le.inverse_transform(temp_encoded) #similarly for weather and play
print(temp)





 



















