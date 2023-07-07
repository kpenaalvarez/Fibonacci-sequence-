# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:52:24 2023

@author: kpenaalvarez
"""

import numpy as np
import matplotlib.pyplot as plt

# define a function that conputes n+1 st fibonnaci, given 
# thhe previous two fibonnaci numbers

def aliens(F, n):
    """
    

    Parameters
    ----------
    F : integer array
        F[n] is the n-th Fibonacci number
    n : integer
        index into F

    Returns
    -------

    """
    F[n] = F[n-1] + F[n-2]
    return F[n]

def aliens2(F, n):
        if len(F) < 2:
            print('F is not long enough')
            return(0)
        F.append(F[n-1]+F[n-2])
        return F[n]
    
if __name__=="__main__":
    
    #first set up an array
        F = np.zeros(100)
        F[0] = 0
        F[1] = 1
        
        for n in range(2, 20):
            F[n] = aliens(F, n)
           
        intF = [int(x) for x in F[:20]]
        print(intF)
        #now use a list
        
        F = []
        F.append(0)
        F.append(1)
        print(F)
        
        for n in range(2,20):
            F[n] = aliens2(F, n)
            print(F[n])
            
# to finish, compute d[n] =F[n]/F and for n=1 to 20 plot d[n]

        d = F
        plt.plot(d,'.')
  
        
