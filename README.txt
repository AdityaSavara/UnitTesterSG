Using the Unit Testing Module (UnitTesterSG):

The unit tester is designed to test individual functions by storing outputs of a working function in an expected results file and comparing this output to the current output of the same function that may have been edited.
This is done so that the user can use his or her expected output to test the function at a later time to make sure the output now is the same as before and that no errors have come up. This module is designed to be able to unit test arrays, strings, as well as nested and deeply nested objects (including arrays with tuples inside, arrays with strings inside, etc.).

Provided are multiple test cases in ExampleFiles: somne have hard coded results while the last one shows how to use write a test file for a function.

The template of what the test file should look like is in test11.py.  This file uses a simple function to sum values in a list together.
To use these examples, make sure UnitTesterSG.py, nestedObjectsFunctions.py, and the eleven testX.py files are in the same directory.  Running UnitTesterSG.py will test all eleven cases.  Note: UnitTesterSG will look for test1.py, test2.py, test3.py... testN.py where N is the number of files in the directory (so if there are 4 unit tests but 11 files, it will print "trying test5, trying test6 ...." even if there are only 4 tests).

You can create an expected results file ahead of time.  More typically, you would check manually that your function is working the first time, and then you would make test1.py, test2.py, etc. files (see examples) then rune UnitTesterSG 
Initially, there will be no "expected results" to check against, so you would choose the "Y" option which will store the results.  Then, in the future, after you edit your function, you can check the revised function's outputs against those stored results by making a copy of the full subdirectory where you did the testing and replacing the version of your module in the fresh copy. Note that your (old) stored results will be in the freshly copied directory, so the unit tester will then compare your revised function's output to the stored output.

Using the customCompare funtion, the unit tester will work with nested objects and strings to show that the pickling worked and the object before and after pickling are the same.


Authors - Savara Group