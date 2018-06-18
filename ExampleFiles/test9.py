# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:07:44 2018

@author: Alex
"""

#import the functions from UnitTesterSG
from UnitTesterSG import *
    
#Extracting the digit from the file name to use as prefix/suffix in check_results
def returnDigitFromFilename():
    import os
    filename = os.path.basename(__file__)
    import re
    listOfNumbers = re.findall('\d+',filename)
    extractedDigit = listOfNumbers[0]
    return extractedDigit


#get the suffix argument for check_results
suffix = returnDigitFromFilename()

#input
import numpy as np
import copy

resultObj = ((1,2),4)


#String is provided
resultStr = str(resultObj)

#run the Unit Tester
check_results(resultObj, resultStr, prefix = '', suffix=suffix)


