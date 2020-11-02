# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:15:45 2020

@author: Masaya Heywood
"""
import numpy as np
import scipy.stats as sp
import sklearn.metrics as sk

dummyList = [3, 4, 5, 8]
dummy2DList = [(0,50), (10,5), (5,10)]
dummyNumpy = np.array(dummyList)
dummy2DNumpy = np.array(dummy2DList)
dummyRand2DNumpy = np.random.rand(100, 2) 

def normalizedError (numberSet, power):    
    """
    Function by Masaya Heywood
    Takes in a 2D numpy array or list (numberSet) and returns normalized error based upon the entered power (power).
    Use numbers 1 to n in power to select if the function returns mean absolute error, RMSE and RMSE to a higher power of any number.
    Entering 0 will return an error.
    """
    
    numberArr = np.array(numberSet) #incase input is not a numpy array
    
    if power == 1:
        output = sk.mean_absolute_error(numberArr[:,0], numberArr[:,1])  
    elif power == 2:  
        #output = np.sqrt(sk.mean_squared_error(numberSet[:,0], numberSet[:,1]))
        output = np.sqrt(((numberArr[:,1] - numberArr[:,0]) ** 2).mean())
    elif power == 0:
        raise ValueError('please have a power greater than 0')
    else:
        output = (((numberArr[:,1] - numberArr[:,0]) ** power).mean())**(1/power)
    return (output)

print(normalizedError(dummy2DList, 1))