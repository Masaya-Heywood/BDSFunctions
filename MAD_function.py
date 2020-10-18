# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 02:07:11 2020

@author: Masaya Heywood

This file contains a function that finds the mean absolute deviation of a one dimensional list or numpy array.
"""

import numpy as np
dummyList = [3, 4, 5, 8]
dummyNumpy = np.array(dummyList)

def calculateMAD (numberSet):
    #Assumes that numberSet is a 1D, numerical list or numpy array, then initiates an empty list and calculates the mean of numberSet.
    
    writtenBy = "Masaya Heywood" #My Name
    absoluteValues = [] 
    numberSetMean = np.mean(numberSet)
    
    #Calculates the absolute value for each element in the set. These values are stored in the empty list made earlier.
    for each in range (len(numberSet)):
        absoluteValues.append(1)
        absoluteValues[each] = abs(numberSet[each] - numberSetMean)
        
    #Calculates and returns the MAD from the new list.
    MAD = sum(absoluteValues)/len(absoluteValues)
    return MAD

testPrint = calculateMAD(dummyNumpy)
print(testPrint)

