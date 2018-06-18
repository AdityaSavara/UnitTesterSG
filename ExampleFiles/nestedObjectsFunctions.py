# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:49:12 2018

@author: Alex
"""
import collections

#This makes the sum of a Nested array/list/tuple.
#For example: [-1, 2, [3, 4, 5], 6] will give 19.
# and [1, 2, [3, 4, 5], 6] will give 21.
def sumNested(arr):
    currentSum = 0
    if isinstance(arr,collections.Iterable):
        for elem in arr:
            returnSum = sumNested(elem)
            currentSum = currentSum + returnSum
        return currentSum
    else:  #if the code has gotten here, the input is a number and the "sum" is just itself.
        sumArr = arr
        return sumArr
    
#This makes the sum of absolute values of a Nested array/list/tuple.
#For example: [-1, 2, [3, 4, 5], 6] will give 21.
# and [1, 2, [3, 4, 5], 6] will give 21.
def sumNestedAbsValues(arrayOrNumber):
    currentSum = 0
    if isinstance(arrayOrNumber,collections.Iterable):
        for elem in arrayOrNumber:
            returnSum = sumNestedAbsValues(elem)
            currentSum = currentSum + returnSum
        return currentSum
    else: #if the code has gotten here, the input is an indivudal number so here is where we take the absolute value.
        AbsVal = abs(arrayOrNumber)
        return AbsVal


#isNestedOrString takes an array and checks to see if it is iterable.  If it is iterable then it loops through the array
#to see if it has any more iterable objects.  If there are no iterable values in the array, then the array is not nested.
#Otherwise it has nesting.
#Examples: 3 is not iterable and will return false
#[1,2] is iterable but neither 1 nor 2 are iterable so isNestedOrString will return false
#[1,[2,3]] is iterable, 1 is not iterable but [2,3] is so isNestedOrString will return true
def isNestedOrString(arr):
    if isinstance(arr,collections.Iterable):
        for elem in arr:
            if isinstance(arr,collections.Iterable):
                return True
        #If it finishes the loop then it hasn't found a non-iterable object and is not nested
        return False
    #If the object is not iterable then it can't be nested
    else:
        return False

'''
This function has an implied return by modifying the array called subtractionResult
Typically subtractionResult would be a deepcopy of one of the two arrays
If there is a tuple or any other immutable type, the subtractNested function will not work
subtractionResult = copy.deepcopy(arr1)
subtractNested(arr1,arr2,subtractionResult)
'''
def subtractNested(arr1,arr2,subtractionResult):
    if isinstance(arr1,collections.Iterable):
        for elemindex,elem in enumerate(arr1):
            if type(elem) == str:
                #The 0 or 1 returned is opposite what is normally done in Python
                #1 is usually true and 0 is usually false 
                if arr1 == arr2:
                    print(elemindex,arr1,arr2)
                    subtractionResult[elemindex] = 0
                else:
                    subtractionResult[elemindex] = 1
            else: 
                if isNestedOrString(elem):
                    subtractNested(arr1[elemindex],arr2[elemindex],subtractionResult[elemindex])
                else:
                    subtractionResult[elemindex] = arr1[elemindex] - arr2[elemindex]
                    #There is an implied return of arr3 since arr3 was overwritten in the function       
                        

#This function converts a nested Structure into a nested list.
#For example, 
# nestedTuple = (1,2,(3,4,(5)),6)
# nestedList = nested_iter_to_nested_list(nestedTuple)
# yields: [1, 2, [3, 4, 5], 6]
def nested_iter_to_nested_list(iterReceived):
    #The first two lines are justs to return the object immediately if it's not an iterable.
    #This is mostly to prevent bugs if someone tries to feed an integer, for example.
    if not isinstance(iterReceived,collections.Iterable):
        return iterReceived
    list_at_this_level = list(iterReceived)
    for elemIndex, elem in enumerate(iterReceived):
        #A string is iterable and a single value in a string is also iterable
        #So check to see if it is not a string to avoid recursion error
        if isinstance(elem,collections.Iterable) and type(elem) != str:
            list_at_this_level[elemIndex] = nested_iter_to_nested_list(elem)
        else:
            list_at_this_level[elemIndex] = elem
    return list_at_this_level

	