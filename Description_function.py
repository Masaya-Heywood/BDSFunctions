# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:13:04 2020

@author: Masaya Heywood
"""
import math
import numpy as np

dummyList = [3, 4, 5, 8]
dummyNumpy = np.array(dummyList)

def calculateMAD (numberSet):
    #Written By Masaya Heywood
    #Assumes that numberSet is a 1D, numerical list or numpy array, then initiates an empty list and calculates the mean of numberSet.
    absoluteValues = [] 
    numberSetMean = np.mean(numberSet)
    
    #Calculates the absolute value for each element in the set. These values are stored in the empty list made earlier.
    for each in range (len(numberSet)):
        absoluteValues.append(1)
        absoluteValues[each] = abs(numberSet[each] - numberSetMean)
        
    #Calculates and returns the MAD from the new list.
    MAD = sum(absoluteValues)/len(absoluteValues)
    return MAD

def calculateDescrip (numberSet):
    #Written By Masaya Heywood
    #Calculates Mean, Median, Standard Deviation, Mean Absolute Deviation and length of the imported number set.
    #Assumes numberSet is a 1D list of numbers or numpy array.
    
    #turns list into an numpy array, if not already and array
    if type(numberSet) == list:
        numberSet = np.array(numberSet)
    
    #Calculations
    setMean = np.mean(numberSet)
    setMedian = np.median(numberSet)
    setSD = np.std(numberSet)
    setMAD = calculateMAD(numberSet)
    setLength = len(numberSet)
    setSEM = setSD / math.sqrt(setLength)
    
    
    resultsArr = np.array([setMean, setMedian, setSD, setMAD, setLength, setSEM])
    
    return (resultsArr)

testPrint = calculateDescrip(dummyNumpy)
print(testPrint)
        
        