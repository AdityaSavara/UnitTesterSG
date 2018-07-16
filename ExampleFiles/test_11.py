# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:07:44 2018

@author: Alex
"""
import sys
sys.path.insert(1, "..\\lib")
sys.path.insert(1, "..")
#import the functions from UnitTesterSG
import UnitTesterSG as ut
#import your function
from sumOfValues import sum_of_elements

#get the suffix argument for check_results
suffix = ut.returnDigitFromFilename(__file__)

#input for the unit that will be tested
input = [1,2,3]

#These two lines can hardcode the expected results. They are not required. 
#expected_results = 6
#ut.set_expected_result(expected_results, str(expected_results), prefix = '', suffix=suffix)

#outputs with the function being tested using the input
output = sum_of_elements(input)

#places the object in a tuple
resultObj = (output)

#String is provided
resultStr = str(resultObj)

#run the Unit Tester
def test_Run(allowOverwrite = False):
    #if the user wants to be able to change what the saved outputs are
    if allowOverwrite:
        #This function call is used when this test is run solo as well as by UnitTesterSG
        ut.check_results(resultObj, resultStr, prefix = '', suffix=suffix)
    #this option allows pytest to call the function
    if not allowOverwrite: 
        #this assert statement is required for the pytest module 
        assert ut.check_results(resultObj, resultStr, prefix = '', suffix=suffix, allowOverwrite = False) == True
    
if __name__ == "__main__":
   test_Run(allowOverwrite = True)
