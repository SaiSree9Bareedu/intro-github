# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:25:58 2020

@author: saisr
"""


# using scipy lib for poission and normal distribution
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import poisson
rv = poisson(2) 
print(rv)


arr =[]
rv = poisson(20)
rv.pmf(3)



for num in range(0,40):
    arr.append(rv.pmf(num))
    
prob = rv.pmf(25)
print(prob)

import matplotlib.pyplot as plt
plt.grid(True)
plt.plot(arr)
plt.plot(25,prob,marker = '.',c ='r')
plt.show()
                        #pmf- probability mass function , pdf- probabilty density function

from scipy.stats import norm

range = np.arange(-3,3,0.001)
plt.plot(range,norm.pdf(range,0,1))
plt.show()   