# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:19:56 2020

@author: Masaya Heywood
"""

import numpy as np
import scipy.stats as sp

dummyList = [3, 4, 5, 8]
dummy2DList = [(300,2000), (4,6), (-53,52), (1200,-80)]
dummyNumpy = np.array(dummyList)
dummy2DNumpy = np.array(dummy2DList)
dummyRand2DNumpy = np.random.rand(100, 2) 

def descriptivesWindow (numberSet, calType, winSize):
    """
    Function by Masaya Heywood
    Takes in a numpy array (numberSet) of either one or two dimensions to return, mean, standard deviation or correlation as an array.
    Use numbers 1 to 3 in calType to select if the function returns mean, standard deviation or correlation respectively.
    Use winSize to determine the scrolling window size (how large you want each selection from the array to be).
    The window will ignore any selections that are larger or smaller than winSize.
    """
    
    #incase these aren't imported
    import numpy as np
    import scipy.stats as sp
    outputArr = np.array([])
    
    #calculates the selection
    for i in range(len(numberSet)):
        selection = numberSet[i : i+winSize]
        
        #ensures that the selection does not select anything more or less than the window size
        if len(selection) == winSize:
        
            if calType == 1:     #calculate the mean and return an array
                outputArr = np.append(outputArr, np.mean(selection))
            
            elif calType == 2:   #calculate the SD and return an array 
                outputArr = np.append(outputArr, np.std(selection))
             
            elif calType == 3:   #calculate the correlations and return an array 
                if len(numberSet.shape) == 2: #check if the numberSet is a 2d Array
                    r, p = sp.pearsonr(selection[:,0], selection[:,1])
                    outputArr = np.append(outputArr, r)
                else:
                    raise ValueError('numberSet must be a 2D array for calType 3 correlations')
            
            #if calType is incorrect, tell error
            else:
                 raise ValueError('calType must be a integer from 1 to 3. 1 for mean, 2 for SD, 3 for correlation')
        else: 
            break
        
        
        
        
    values = 0
    return (outputArr)


print(descriptivesWindow(dummyRand2DNumpy, 1, 1))