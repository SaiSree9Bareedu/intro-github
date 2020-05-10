# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:45:02 2020

@author: saisr
"""


import pandas as pd
import numpy as np

tables = pd.read_html("fdic_failed_bank_list.html")
print(tables)
failures = tables[0]

d = pd.to_datetime(failures["Closing Date"])
print(d)

f = pd.ExcelFile("ex1.xlsx")
print(f)
f = pd.read_excel("ex1.xlsx")

s = f.drop(columns = "Unnamed: 0",inplace = True)
print(s)

import requests
url = "https://api.github.com/repos/pandas-dev/pandas/issues"
r = requests.get(url)
print(r)
  
import json
v = r.json()
print(v)

issues = pd.DataFrame(v,columns = ["number","title","state","labels"])
issues.head()
print(issues)

import sqlite3
query = "CREATE TABLE exam(a VARCHAR(20),b VARCHAR(20),c REAL,d INTEGER)";
con = sqlite3.connect("mydata.sqlite")
con.execute(query)
con.commit()

data = [("aber","dude",2.3,6),("sins","boons",4.5,2),("seses","buss",2.78,1)]
stmt = "INSERT INTO exam VALUES(?,?,?,?)"
con.executemany(stmt,data)
con.commit()
cursor = con.execute("SELECT * FROM exam")
print(cursor)
rows = cursor.fetchall()
print(rows)

import matplotlib.pyplot as plt
data = [1,2,3,4,5]
plt.plot(data)

import matplotlib.pyplot as plt
data = [1,2,3,4,5]
plt.plot(data,'.')

from matplotlib import style
x = plt.style.available
print(x)
from matplotlib import style
style.use("_classic_test")
plt.bar([1,2,3,4,5],[2,5,4,8,1],label = "caseone",color = 'r')
plt.bar([3,5,1,7,8],[1,9,3,2,5],label = "casetwo",color = 'b')
plt.legend('best')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("cases")
plt.show()

pop_data = [12,20,30,60,40,39,50,68,30,20,60,12,40,40,30,80,60,60,80]
bins = [10,20,30,40,50,60,70,80]
plt.hist(pop_data,bins,histtype = 'barstacked',rwidth = 0.5)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("histgrma")

hobb = ['eat','chleep','play','laugh']
s = [20,10,40,30]
cols = ['c','m','y','k']
plt.pie(s,labels = hobb,colors = cols,startangle = 90,shadow = True,explode = (0,0,1.0,0),autopct = "%1.1f%%")
plt.title("piechart")
plt.show()

a =[2,5,7,8]
b= [1,7,9,3]
c= [7,3,2,8]
d = [5,8,1,7]
e = [2,8,5,7]
plt.stackplot(a,b,c,d,e, colors = ['c','m','y','k'])
plt.show()


o = pd.read_csv("top-five-wine-score-counts.csv")
print(o).head()
