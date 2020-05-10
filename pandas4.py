# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:00:12 2020

@author: saisr
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import plotly

x = plotly.__version__
print(x)

from plotly.graph_objs import Scatter,Layout
plotly.offline.plot({"data":[Scatter(x=[1,2,3,4],y =[4,3,2,7])],"layout":Layout(title ="Hello World")})
plt.show()

import plotly.graph_objs as go

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

trace = go.Scatter(x = random_x,y = random_y, mode = "markers")
data = [trace]
plotly.offline.plot(data,filename = "myfirstplotlyonline.html") #these html plots are present in this github repository
plt.show()

from datetime import *

a = datetime.now()
print(a)

delta= datetime(2019,3,15)-datetime(2020,2,20,13,45)
print(delta)

delta.minutes

value = "21 Dec 1995"

print(value)

dates = [datetime(2011,3,19),datetime(2011,3,15),datetime(2011,3,2)]
a = pd.Series(np.arange(3),index = dates)
print(a)

#how to take a 76 days data of a year
r = pd.Series(np.random.randn(76),index = pd.date_range("1,3,2019",periods = 76))
print(r)

s = pd.date_range("1,3,2019",periods=100,freq ="W-SAT" ) 
print(s)

l = pd.DataFrame(np.random.randn(100,4),index = s,columns = ["XOX","MOM","DOD","BOB"])
print(l)







 























