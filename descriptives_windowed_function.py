# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:19:56 2020

@author: Captworgen
"""

import math
import numpy as np

dummyList = [3, 4, 5, 8]
dummy2DList = [(3,2), (4,6), (5,5), (1,8)]
dummyNumpy = np.array(dummyList)
dummy2DNumpy = np.array(dummy2DList)

def descriptivesWindow (numberSet, calType, winSize):
    if calType == 1:
        
        # for the window size, calculate the mean and return an array 
        numberSetMean = np.mean(numberSet)
    elif calType == 2:
        
         # for the window size, calculate the SD and return an array 
        values = 2
    elif calType == 3:
        if type(numberSet) == len(numberSet.shape):
             values = 0
             #calculate the correlation
        else:
            raise ValueError('numberSet must be a 2D array for calType 3 correlations')
        values = 0
    else: 
        raise ValueError('calType must be a integer from 1 to 3. 1 for mean, 2 for SD, 3 for correlation')
        
        
        
        
    values = 0
    return (values)