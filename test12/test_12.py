# -*- coding: utf-8 -*-
"""
There are two ways to use UnitTesterSG: either with a known expected response, or simply comparing to a stored response.
Here, we will show a case with a known (e.g., analytical or otherwise calculated) expected response.
You may copy this file and modify it to make your own test. Just name your file test_N where N is an integer.

#NOTE: WHEN YOU RUN THIS FILE, IT WILL SAY THE **EXPECTED RESULT** MATCHES BUT THAT THE **EXPECTED RESULT STRING** DOES NOT MATCH.
#IT IS PERFECTLY FINE THAT THE RESULT STRING DOES NOT MATCH. THAT IS A TYPICAL SITUATION AND A FEATURE. IT DOES NOT MEAN THE TEST FAILED.
"""

#These "sys" lines are mainly because this are standard lines in our examples. Normally, you would not include these three lines.
import sys
sys.path.insert(1, ".\\lib")
sys.path.insert(1, "..")



#import the functions from UnitTesterSG
import UnitTesterSG as ut

#The below lines are typical code. There is no need to modify them.
#get the suffix argument for check_results
suffix = ut.returnDigitFromFilename(__file__)
#prefix. Make this '' if you do not want any prefix.
prefix = ''


"""
#Now, let's assume you ***know*** what result you expect.
#Let's say it's a scientific problem where you will put in the number 4, and you will get two arrays out. One with values  [3,4,5]  and another with [32,64] Note that they are of different lengths.
#We must make a single results object: we will put lists with those values inside.
#Recognize that we are expecting array objects, but we can define our analytical result as a list.
"""
#input for the unit that will be tested
input = 4
expectedFirstPart = [3,4,5]
expectedSecondPart = [32,64]
expectedResult = (expectedFirstPart,expectedSecondPart) #We are using a tuple, but it this could have been a list.

ut.set_expected_result(expectedResult,expected_result_str=str(expectedResult), prefix=prefix,suffix=suffix) #This is the typical syntax if you want to force an analytical result for your test.


"""
#Calculate your function outputs. We'll use some functions for our fictional scientific problem. You would call real functions from another module.
"""
import numpy as np
def calculationFirstPart(inputNumber):
    if inputNumber == 4:
        return 3.0000001+np.array([0,1,2]) #This will return an array similar to [3,4,5]. Believe me. We are intentionally using non integer values to demonstrate the tolerances feature.

def calculationSecondPart(inputNumber):
    if inputNumber == 4:
        return 32.00000001*np.array([1.,2.]) #This will return an array similar to [32,64]. Believe me. We are intentionally using non integer values to demonstrate the tolerances feature.

#input = 4 #This input is the same as above. Just reproduced for clarity. 
#outputs with the function being tested using the input
outputFirstPart = calculationFirstPart(input)
outputSecondPart = calculationSecondPart(input)
actualResult = (outputFirstPart, outputSecondPart)

"""Put your actual result into the resultObj variable."""
#put this in the resultObject
resultObj = actualResult

#String must be provided provided. Make it '' if you do not want to use a result string.
resultStr = str(resultObj)


"""Normally you will never touch the below lines except to change or make tolerances."""
relativeTolerance = 1.0E-5
absoluteTolerance = 1.0E-8


#this is so that pytest can do UnitTesterSG tests.
def test_pytest(): #note that it cannot have any required arguments for pytest to use it, and that it is using variables that are defined above in the module.
    ut.doTest(resultObj, resultStr, prefix=prefix,suffix=suffix, allowOverwrite = False, relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance)
    
    
if __name__ == "__main__":
   #This is the normal way of using the UnitTesterSG module, and will be run by UnitTesterSG or by running this test file by itself.
   ut.doTest(resultObj, resultStr, prefix=prefix,suffix=suffix, allowOverwrite = True, relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance)
