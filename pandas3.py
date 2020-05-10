# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:30:06 2020

@author: saisr
"""

import seaborn as sns

a = sns.get_dataset_names()
print(a)

d = sns.load_dataset("planets")
d.head()
print(d)

a = sns.axes_style()
print(a)

import matplotlib.pyplot as plt
import numpy as np, pandas as pd;
sns.set(style = "darkgrid",color_codes = True)
attention = sns.load_dataset("attention")
attention.head()
print(attention)
g = sns.jointplot(x = "subject",y = "score",data = attention ,kind = "resid")

sns.set(style = "ticks")
iris = sns.load_dataset("iris")
print(iris.head())
g = sns.pairplot(iris,hue = "species", diag_kind = "hist", kind = "scatter",palette = "husl",markers = ['+','D','*'])

d = sns.pairplot(iris,vars = ["petal_length","petal_width"])

sns.set(style="ticks")
f = sns.load_dataset("planets")
print(f.head())
g = sns.barplot( x = "method",y = "distance", data = f)

sns.set(style="ticks")
attention = sns.load_dataset("attention")
print(attention.head())
g = sns.boxplot(x = attention["score"])


sns.set(style="ticks")
tips = sns.load_dataset("tips")
print(tips.head())
g = sns.boxplot(x = tips["days"])
ax = sns.boxplot( x= "day",y = "tip", data = tips)

ax = sns.boxplot( x= "day",y = "tip", data = tips , hue = "smoker",palette = "husl")

ax = sns.boxplot(data = tips,palette = "Set3",orient = "h")

g = sns.stripplot(data = iris)
g = sns.stripplot(data = iris , x = "species",y = "petal_width")
g = sns.swarmplot(data = iris , x = "species",y = "petal_width")
plt.show()

sns.set_context("paper",font_scale = 2,rc ={"font.size":0.6,"axes_labelsize":6})
plt.show()
































