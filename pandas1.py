# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:30:19 2020

@author: saisr
"""

#initially we need to import numpy and pandas libraries
import numpy as np
import pandas as pd

name = np.array(['A','m','s','t','e','r','d','a','m'])
print(name)

n = pd.Series(name,index = [1,2,3,4,5,6,7,8,9]) #building a dataframe of this 1 dimensional data 'name'
                                                 # and also giving indexes to it
print(n)

dic = pd.Series({'key': 1,'lock': 2 ,'screw': 3})
print(dic)

dic = pd.Series(['zoom','normal','parallel'],index = [0,1,2])
print(dic)

data = pd.DataFrame([3,4,5,6,7],[1,2,3,4,5])
print(data)

pop = {'Country':['China','India','Japan'],'Male':[3000,3050,4000],'Female':[4500,1000,5000],'Dual':[200,300,400]}
dum = pd.DataFrame(pop,columns = ['Country','Male','Female','Dual'],index = [1,2,3],dtype = float)
print(dum)

pop = {'Country':pd.Series(['China','India','Japan'],index = [1,2,3]),'Male':pd.Series([3000,3050,4000,2000],index = [1,2,3,4]),'Female':pd.Series([4500,1000],index = [1,2])}
dum = pd.DataFrame(pop)
print(dum)

obj = pd.Series(['sai','sree',23,45],index = ['a','b','c','d'])
print(obj)

obj[['a','d']] = ['sui',37]
print(obj)

d = obj['c']
print(d)

h = obj.index
print(h)

c = obj>0
print(c)

obj = pd.Series([0,-2.3,23,45],index = ['a','b','c','d'])
c = obj[obj>0]
print(c)

f = np.exp(obj)
print(f)

d = np.sqrt(obj)
print(d)

s = pd.notnull(obj)
print(s)

car = {'SUV':['Duster','Fortuner','Hummer','Bolero','Jeep'],'Year':[2010,2012,2015,2008,2018],'Mileage_in_kmph': [300,500,800,900,1000]}
frame_1 = pd.DataFrame(car)
print(frame_1)

car = {'SUV':['Duster','Fortuner','Hummer','Bolero','Jeep'],'Year':[2010,2012,2015,2008,2018],'Mileage_in_kmph': [300,500,800,900,1000]}
frame_1 = pd.DataFrame(car,columns = ['Mileage_in_kmph','Year','SUV','Loss'],index = ['a','b','c','d','e'])
print(frame_1)

data = pd.Series(range(5), index = ['a','b','c','d','e'])
print(data)

label = pd.Index(np.arange(3))
dat = pd.Series(['eat','sleep','repeat'],index = label)
print(dat)

dat.index = label

super = pd.DataFrame(np.arange(4).reshape(-2,2),index = ['a','b'], columns = ['fam','jam'])
print(super)

a = super.drop(['b'])
print(a)

s = super.drop('fam',axis = 1)
print(s)

w = pd.DataFrame(np.arange(16).reshape(-1,4),index = ['a','b','c','d'],columns = ["india","russia","africa","britan"])
print(w)

q = pd.DataFrame(np.random.randn(4,3),index = ['a','c','e','f'], columns = ["A","B","C"])
print(q)

r = q.reindex(['a','b','c','d','e','f'])
print(r)

s = r.fillna(method = 'bfill',axis = 0)
print(s)

t = s.fillna(method= "ffill",axis =1).fillna(4)
print(t)

u = pd.DataFrame({'values' : [2,3,5,np.nan,np.nan,np.nan,8,1,np.nan],
                 'columns' : ['A','A','B','B','C','C','C','C','D'],
                 'index' : list('mmmmnnnoo')})
print(u)


u['values'] = u.groupby(['columns','index'])['values'].apply(lambda x : x.fillna(x.mean()))
print(u)























