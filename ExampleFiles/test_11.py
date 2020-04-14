# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:07:44 2018

@author: Alex
"""
import sys
sys.path.insert(1, ".\\lib") #TODO: This should be made into a relative path, to be more compatible with pytest.
sys.path.insert(1, "..")
#import the functions from UnitTesterSG
import UnitTesterSG as ut
#import your function
from sumOfValues import sum_of_elements

#get the suffix argument for check_results
suffix = ut.returnDigitFromFilename(__file__)
#prefix. Make this '' if you do not want any prefix.
prefix = ''

#input for the unit that will be tested
input = [1,2,3]

#These two lines can hardcode the expected results. They are not required. 
#expected_results = 6
#ut.set_expected_result(expected_results, str(expected_results), prefix = '', suffix=suffix)

#outputs with the function being tested using the input
output = sum_of_elements(input)

#places the object in a tuple
resultObj = (output)

#String must be provided provided. Make it '' if you do not want to use a result string.
resultStr = str(resultObj)

#this is so that pytest can do UnitTesterSG tests.
def test_pytest(): #note that it cannot have any required arguments for pytest to use it, and that it is using variables that are defined above in the module.
    ut.doTest(resultObj, resultStr, prefix=prefix,suffix=suffix, allowOverwrite = False)
    
    
if __name__ == "__main__":
   #This is the normal way of using the UnitTesterSG module, and will be run by UnitTesterSG or by running this test file by itself.
   ut.doTest(resultObj, resultStr, prefix=prefix,suffix=suffix, allowOverwrite = True)
