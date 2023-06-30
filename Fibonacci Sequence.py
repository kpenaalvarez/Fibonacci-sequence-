# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:41:31 2023

@author: kpenaalvarez
"""
import matplotlib.pyplot as plt
import numpy as np

n = 100
a = 0
b = 1
s = 0
fibseq = []
for x in range(n):
    fibseq.append(s)
    print(s,end=" ")
    s = a+b
    b = a
    a = s
plt.xlim(0, 20)
plt.ylim(0,2500)
plt.plot(fibseq, color='red')
plt.xlabel('Index')
plt.ylabel('Fibonacci Number')
plt.title('Fibonacci Sequence')
plt.show()
