# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:08:05 2017

@author: tienhung2501
"""

import numpy as np
import collections
import copy
from nestedObjectsFunctions import *


'''
customCompare takes in two values and compares them based on their types
If both inputs are strings, customCompare just simply compares the two with ==.
If both inputs are not strings and they are both iterable, customCompare will convert the two
values to arrays and compare them by taking the difference of the two arrays and adding up all the
values.  If the arrays are the same then the sum of the differences should be 0.
If both inputs are not strings but one is iterable and one is not, customCompare returns False.  This should occur
the first time the unit tester is run because the expected results file will not have been created so it is of type None.
If both inputs are not strings nor are they iterable, customCompare checks the equality using ==.
'''
def customCompare(firstInComparison,secondInComparison):
	#If two variables are both strings, just simply compare them directly
    if ((type(firstInComparison) != str) and (type(secondInComparison) != str)):
		#checks to see if both variables are iterable and converts them into numpy arrays
        if isinstance(firstInComparison,collections.Iterable) and isinstance(secondInComparison,collections.Iterable):
            firstInComparisonArray = np.array(firstInComparison)
            secondInComparisonArray = np.array(secondInComparison)
            
                
                #Taking the difference of two arrays will yield in all elements being zero if the arrays are the same
            try:    
                #Initializing diffOfArrays since it is needed for the subtractNested function
                diffOfArrays = nested_iter_to_nested_list(copy.deepcopy(firstInComparisonArray))
                #If the arrays are the same, subtractNested overwrites diffOfArrays with all zeros
                #If there is a tuple or any other immutable type, the subtractNested function will not work
                subtractNested(firstInComparisonArray,secondInComparisonArray,diffOfArrays)
				
            except:
                return False
            #The difference sum keeps adding all the values until it no longer has an array
            sumOfDifference = sumNestedAbsValues(diffOfArrays)
            
            #If the two arrays are equal, then the sum of the differences Array should be zero
            if sumOfDifference == 0:
                return True
            else:
                return False
                

		#checks to see if one, not both, of the variables are iterable
		#this is for the case with one variable being None
        elif isinstance(firstInComparison,collections.Iterable) or isinstance(secondInComparison,collections.Iterable):
                return False
		#runs if neither of the variables are iterables or if they are both strings
        else:
			#if comparison can not run then types are probably different and returns false
            try:
                comparison = (firstInComparison == secondInComparison)
                return comparison
            except:
                return False
    else:
        if firstInComparison == secondInComparison:
            return True
        else:
            return False


def check_results(calculated_resultObj,calculated_resultStr='',prefix='',suffix=''):
    import pickle
    calculated_resultObj_pickledfile='{}calculated_resultObj{}.p'.format(prefix,suffix)
    calculated_resultStr_file='{}calculated_resultStr{}.txt'.format(prefix,suffix)
    expected_result_file='{}expected_resultObj{}.p'.format(prefix,suffix)
    expected_resultStr_file='{}expected_resultStr{}.txt'.format(prefix,suffix)
    #pickling and writing the result object
    with open(calculated_resultObj_pickledfile,'wb') as pickled_calculated_result:
        pickle.dump(calculated_resultObj,pickled_calculated_result)
    #reading and unpack the pickled result object
    with open(calculated_resultObj_pickledfile,'rb') as pickled_calculated_result_after:
        calculated_resultObj_unpacked=pickle.load(pickled_calculated_result_after)
    #comparing from pickled and before
    
    #if calculated_resultObj_unpacked==calculated_resultObj:
    if customCompare(calculated_resultObj_unpacked,calculated_resultObj) == True:
        print('calculated_Results before and after pickling match.')
    else:
        print("calculated_Results before and after pickling don't match. (or is nested)")
    #Writing the string results:
    with open(calculated_resultStr_file,'w') as calculated_result_str:
        calculated_result_str.write(calculated_resultStr)
    #reading the string from text file
    with open(calculated_resultStr_file,'r') as calculated_result_str_after:
        calculated_resultStr_read=str(calculated_result_str_after.read())
    #comparing calculated_results string before and after writing to text file
    if calculated_resultStr==calculated_resultStr_read:
        print('String calculated_results before and after writing match.')
    else:
        print("String calculated_results before and after writing don't match.")
    #try and except are for asigning the expected results variable
    try:
        #checking the expected result string
        with open (expected_resultStr_file,'r') as expected_resultStr:
            expected_resultStr_read=str(expected_resultStr.read())
        #Checking expected result object after pickling vs. before pickling
        with open (expected_result_file,'rb') as expected_resultObj:
            expected_resultObj_unpacked=pickle.load(expected_resultObj)
    except: #This is for if the expected results files are not already there.
        expected_resultStr_read=''
        expected_resultObj_unpacked=None
    #compare the expected result to the calculated result, both obj and str
    if customCompare(expected_resultObj_unpacked,calculated_resultObj_unpacked) == True:
        print('Expected result matches calculated_result.')
    else:
        print('Expected result does not match calculated_result. (or is nested)')
    if expected_resultStr_read==calculated_resultStr_read:
        print('Expected result string matches calculated_result string')
    else:
        print('Expected result string (top) does not match calculated_result string (bottom)')
        print(expected_resultStr_read)
        print(calculated_resultStr_read)
        overwritechoice=str(input('Overwrite (or create) the expected result file from the calculated results provided (Y or N)? '))
        if str(overwritechoice)=='Y':
            #pickling the calculated result into the expected result file
            with open(expected_result_file,'wb') as expected_resultObj:
                pickle.dump(calculated_resultObj_unpacked,expected_resultObj)
            with open(expected_resultStr_file,'w') as expected_resultStr:
                expected_resultStr.write(calculated_resultStr_read)
        elif str(overwritechoice)=='N':
            pass    
        else:
            print("Error: Only Y or N allowed. Please run program again.")

if __name__=="__main__":
    import os
    working_dir=os.getcwd()
    number_of_files=len(os.listdir(working_dir))
    for  i in range(1,number_of_files+1):
        try:
            print("Trying Test" + str(i))
            exec('import test{}'.format(i))
        except ImportError:
            pass
