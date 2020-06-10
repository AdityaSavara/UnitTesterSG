# -*- coding: utf-8 -*-
"""
There are two ways to use UnitTesterSG: either with a known expected response, or simply comparing to a stored response.
Here, we will show a case where we compare to an **existing from before** output.

TO USE THIS WAY OF DOING THINGS, YOU MUST RUN YOUR FILE ONE TIME TO INITIATE (IN THIS CASE RUN test_13.py)
THE FIRST TIME THIS FILE IS RUN, IT WILL SAY THAT THE CALCULATED RESULT AND EXPECTED RESULT DO NOT MATCH, BECAUSE THE EXPECTED RESULT DOES NOT EXIST.
THE SECOND QUESTION THE PROGRAM ASKS WILL BE IF YOU WANT TO OVERRWRITE OR CREATE EXPECTED RESULTS FILES: CHOOSE "Y"
NOW, THE EXPECTED RESULT HAS BEEN SET.  RUN THE TEST AGAIN (test_13.py) AND THIS TIME THE TEST WILL PASS.

TO RESET THIS EXAMPLE, DELETE THE FILES THAT BEGIN WITH THE WORD EXPECTED.

You may copy this file and modify it to make your own test. Just name your file test_N where N is an integer.
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
#Now, let's assume you ***don't have an analytical result*** but you know your function is working.
#We know our function is working because we are just using the test 12 example.
In this case, we ***will not*** use the "set_expected_result" command. So we are commenting out he below lines, and will go directly to using the function to create an actual output.
"""
# # # #input for the unit that will be tested
# # # input = 4
# # # expectedFirstPart = [3,4,5]
# # # expectedSecondPart = [32,64]
# # # expectedResult = (expectedFirstPart,expectedSecondPart) #We are using a tuple, but it this could have been a list.

# # # ut.set_expected_result(expectedResult,expected_result_str=str(expectedResult), prefix=prefix,suffix=suffix) #This is the typical syntax if you want to force an analytical result for your test.


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

input = 4 #This input is the same as above. Just reproduced for clarity. 
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
