# -*- coding: utf-8 -*-
#Version 3.3
"""
Created on Wed Nov 22 14:08:05 2017

@author: tienhung2501
"""

import numpy as np
import collections
import copy
from nestedObjectsFunctions import *
import pickle

'''
This function takes in two arrarys (or iterables) and compares them using functions from the nestedObjectsFunctions module
'''
def compareNested(firstInComparisonArray,secondInComparisonArray,diffOfArrays, relativeTolerance=None, absoluteTolerance=None):
        #Taking the difference of two arrays will yield in all elements being zero if the arrays are the same
        #If arrays are of different shape they will not be equal and the subtraction between the two will result in an error
    try:    
                    #Initializing diffOfArrays since it is needed for the subtractNested function
        diffOfArrays = nested_iter_to_nested_list(copy.deepcopy(firstInComparisonArray))
        #If the arrays are the same, subtractNested overwrites diffOfArrays with all zeros
        subtractNested(firstInComparisonArray,secondInComparisonArray,diffOfArrays, relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance)
    except:
        return False
    #The difference sum keeps adding all the values until it no longer has an array
    sumOfDifference = sumNestedAbsValues(diffOfArrays)
    #If the two arrays are equal, then the sum of the differences Array should be zero
    if sumOfDifference == 0:
        return True
    else:
        return False


'''
customCompare takes in two values and compares them based on their types
If both inputs are strings, customCompare just simply compares the two with ==.
If both inputs are not strings and they are both iterable, customCompare will convert the two
values to arrays and compare them by taking the difference of the two arrays and adding up all the
values.  If the arrays are the same then the sum of the differences should be 0.
If both inputs are not strings but one is iterable and one is not, customCompare returns False.  This should occur
the first time the unit tester is run because the expected results file will not have been created so it is of type None.
If both inputs are not strings nor are they iterable, customCompare checks the equality using ==.
#we do allow approximate comparisons using the variables relativeTolerance and absoluteTolerance
'''
def customCompare(firstInComparison,secondInComparison, relativeTolerance=None, absoluteTolerance=None):
    #If two variables are both strings, just simply compare them directly
    if ((type(firstInComparison) != str) and (type(secondInComparison) != str)):
        #checks to see if both variables are iterable and converts them into numpy arrays
        if isinstance(firstInComparison,collections.Iterable) and isinstance(secondInComparison,collections.Iterable):
            try:
                firstInComparisonArray = np.array(firstInComparison)
                secondInComparisonArray = np.array(secondInComparison)
                #If arrays are not nested then simple subtraction using the - operator will work
                #Otherwise use nested array functions
                try:
                    #diffOfArrays will be an array of zeros if the two arrays are equal
                    if (relativeTolerance==None and absoluteTolerance==None):
                        diffOfArrays = firstInComparisonArray - secondInComparisonArray
                    else: #Else one of the tolerances requested is not None
                        import numpy as np 
                        #we 1st need to make any tolerances that are still none into the numpy default, because we don't know if the person has selected both tolerances.
                        #and we cannot feed "None" into numpy.
                        if relativeTolerance == None:
                            relativeTolerance = 1.0E-5
                        if absoluteTolerance == None:
                            absoluteTolerance = 1.0E-8
                        trueIfApproximatelyEqual = np.allclose(firstInComparisonArray,secondInComparisonArray, rtol = relativeTolerance, atol = absoluteTolerance)
                        if trueIfApproximatelyEqual == True:
                            diffOfArrays = 0
                        if trueIfApproximatelyEqual == False: #return actual subtraction if they are not approximately equal.
                            diffOfArrays = firstInComparisonArray - secondInComparisonArray
                    #take the sum of the differences
                    sumOfDifference = sumNestedAbsValues(diffOfArrays)
                    #If the sum of differences is 0 then the two arrays must be the same
                    #Otherwise they have different values and customCompare returns False
                    if sumOfDifference == 0:
                        return True
                    else:
                        return False
                except: 
                    if compareNested(firstInComparisonArray,secondInComparisonArray,diffOfArrays, relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance):
                        return True
                    else:
                        return False
            #Try to convert to an array, if this can not be done it is probably a nested tuple or nested list
            #Functions in the nestedObjectFunctions module do work with nested tuples and lists so the except statement tells the code to do just that
            except:
                diffOfArrays = copy.deepcopy(firstInComparison)
                if compareNested(firstInComparison,secondInComparison,diffOfArrays, relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance):
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


def check_results(calculated_resultObj,calculated_resultStr='',prefix='',suffix='', allowOverwrite = True, relativeTolerance=None, absoluteTolerance=None):
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
    if customCompare(calculated_resultObj_unpacked,calculated_resultObj, relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance) == True:
        print('calculated_Results before and after pickling MATCH.')
    else:
        print("calculated_Results before and after pickling DO NOT MATCH (or is nested and/or contains an unsupported datatype).")
    #Writing the string results:
    with open(calculated_resultStr_file,'w') as calculated_result_str:
        calculated_result_str.write(calculated_resultStr)
    #reading the string from text file
    with open(calculated_resultStr_file,'r') as calculated_result_str_after:
        calculated_resultStr_read=str(calculated_result_str_after.read())
    #comparing calculated_results string before and after writing to text file
    if calculated_resultStr==calculated_resultStr_read:
        print('String calculated_results before and after writing MATCH.')
    else:
        print("String calculated_results before and after writing DO NOT MATCH.")
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
    if customCompare(expected_resultObj_unpacked,calculated_resultObj_unpacked, relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance) == True:
        print('Expected result and calculated_result MATCH.')
        objectMatch = True
    else: #implies that customCompare returned false.
        print("Expected result and calculated_result DO NOT MATCH (or is nested and/or contains an unsupported datatype).")
        objectMatch = False
    if expected_resultStr_read==calculated_resultStr_read:
        print('Expected result string and calculated_result string MATCH')
        stringMatch = True
    else: #implies that expected results string does not match calculated result string.
        stringMatch = False
    if (objectMatch == False) and (stringMatch == True):
        print("Warning: Strings can match for long/large arrays even if objects don't")
    if (objectMatch == False) or (stringMatch == False): #if either object or string comparison failed, we consider overwriting old files.
        #the if statement is to prevent pytest from needing user input. Perhaps should be changed to "interactiveTesting = True" rather than allowOverwrite = True.
        if allowOverwrite:
            if expected_resultStr_read!=calculated_resultStr_read:	#We give the option the user to print out the strings if the string comparison failed.
                printStringsChoice=str(input('Expected result string does not match calculated_result string. Would you like to print them here now to inspect (Y or N)?'))
                if str(printStringsChoice) == 'Y':
                    print('Expected result string (top) DOES NOT MATCH calculated_result string (bottom)')
                    print(expected_resultStr_read)
                    print(calculated_resultStr_read)
            overwritechoice=str(input('Overwrite (or create) the expected result object and string files from the calculated results provided (Y or N)? '))
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
    return objectMatch
			
# skip running the whole program and just set the expected result
def set_expected_result(expected_result_obj,expected_result_str='',
                        prefix='',suffix=''):
    expected_result_obj_file='{}expected_resultObj{}.p'.format(prefix,suffix)
    expected_result_str_file='{}expected_resultStr{}.txt'.format(prefix,suffix)
    with open(expected_result_obj_file,'wb') as expected_result_file:
        pickle.dump(expected_result_obj,expected_result_file)
    with open(expected_result_str_file,'w') as expected_result_file:
        expected_result_file.write(expected_result_str)


#Extracting the digit from the file name to use as prefix/suffix in check_results
def returnDigitFromFilename(currentFile):
    import os
    filename = os.path.basename(currentFile)
    import re
    listOfNumbers = re.findall('\d+',filename)
    extractedDigit = listOfNumbers[0]
    return extractedDigit

def doTest(resultObj, resultStr, prefix='',suffix='', allowOverwrite = False, relativeTolerance=None, absoluteTolerance=None):
    #if the user wants to be able to change what the saved outputs are
    if allowOverwrite:
        #This function call is used when this test is run solo as well as by UnitTesterSG
        check_results(resultObj, resultStr, prefix = '', suffix=suffix, relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance)
    #this option allows pytest to call the function
    if not allowOverwrite: 
        #this assert statement is required for the pytest module 
        assert check_results(resultObj, resultStr, prefix = '', suffix=suffix, allowOverwrite = False,  
               relativeTolerance=relativeTolerance, absoluteTolerance=absoluteTolerance) == True #This line is still part of assert.
    
def runTestsInSubdirectories():
    listOfDirectoriesAndFiles = os.listdir(".")
    #Below is going to become a list of directories only in the next loop.
    directoryList = []
    for elem in listOfDirectoriesAndFiles:
        if os.path.isdir(elem) == True:
            directoryList.append(elem)
    
    #This loop goes into each directories, runs the specified command, and comes back.
    for directory in directoryList:
        print("\nChanging directory to "+directory)
        os.chdir(directory)
        listOfFilesInDirectory=os.listdir(".")\
        
        #Loops through each of the files in the directory and runs any file that begins with 'test_'
        for name in listOfFilesInDirectory:
            if "test_" in name:
                print('\n'+ name)
                os.system("python " + name)
                
        os.chdir("..")
    
    return

if __name__=="__main__":
    import os
    working_dir=os.getcwd()
    filesInDirectory=os.listdir(working_dir)
    for name in filesInDirectory:
        if "test_"in name:
            print('\n'+ name)
            os.system("python " + name)
            
    runTestsInSubdirectories()
