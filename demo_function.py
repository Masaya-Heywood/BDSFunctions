# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 02:38:57 2020

@author: Captworgen
"""
import numpy as np
import scipy.stats as sp
import sklearn.metrics as sk

dummyList = [3, 4, 5, 8]
dummy2DList = [(0,50), (10,5), (5,10)]
dummyNumpy = np.array(dummyList)
dummy2DNumpy = np.array(dummy2DList)
dummyRand2DNumpy = np.random.rand(100, 2) 

def demoFunc (numberSet, power):    
    """
    Function by Masaya Heywood
    Takes in a 2D numpy array or list (numberSet) and returns foo.
    foo line
    foo line
    """
    output = 0
    
    if power == 1:
        output = 1  
    elif power == 2:  
        output = 1  
    elif power == 0:
        raise ValueError('this is a demo error')
    else:
        output = "it's not 1 or 2 or 0"

    for each in len(numberSet):
        output += 1

    return (output)
