# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 04:09:56 2020

@author: Masaya Heywood
"""

import numpy as np
import pandas as pd
import scipy.stats as sp
import sklearn.metrics as sk

dummyList = [3, 4, 4, 5, 8, 5]
dummy2DList = [(0,50), (10,5), (5,10)]
dummyNumpy = np.array(dummyList)
dummy2DNumpy = np.array(dummy2DList)
dummyRand2DNumpy = np.random.rand(100, 2) 

def catCount (numberSet):    
    """
    Function by Masaya Heywood
    Takes in a 1D numpy array or list (numberSet) and returns a 2D array detailing the entry and count of entries (Unique value, amount of values).
    The returned value will be displayed in ascending order based on the value of the entry.
    """
    
    ##importing incase these are not imported
    from collections import Counter
    import numpy as np

    output = []
    uniqueValue = list(Counter(numberSet).values())
    valueCount = list(Counter(numberSet).keys())
    Counter(numberSet).keys()
    
                       
    for each in range(len(uniqueValue)):
        output.append(1)
        output[each] = (valueCount[each], uniqueValue[each])
        
    return (sorted(output,key=lambda l:l[0]))

print(catCount(dummyNumpy))