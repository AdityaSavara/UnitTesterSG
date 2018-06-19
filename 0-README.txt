Using the Unit Testing Module (UnitTesterSG):

The unit tester is designed to test individual functions by storing outputs of a working function in an expected results file and comparing this output to the current output of the same function that may have been edited.
This is done so that the user can use his or her expected output to test the function at a later time to make sure the output now is the same as before and that no errors have come up.

Provided are 11 test cases in ExampleFiles

The template of what the test file should look like is in test11.py.  This file uses a simple function to sum values in a list together.

To use these examples, make sure UnitTesterSG.py, nestedObjectsFunctions.py, and the eleven test.py files are in the same directory.  Run UnitTesterSG and it will test all eleven cases.

The first time running the unit tester will say your calculated output does not match your expected output.  This is because the expected output files do not exist.  You can overwrite
these files by inputting Y so they will store your expected output.  UnitTesterSG uses pickling so any type of data will work in this module.  
Input is dumped into a calculated object file via pickling and then loaded back into the module.  The two objects are compared to ensure pickling worked.

Using the customCompare funtion, the unit tester will work with nested objects and strings to show that the pickling worked and the object before and after pickling are the same.

To use unit tester with your function, open up a new .py file and use the example test files as a template.  Here you can import your function, put in a proper input, and run the unit tester
to check your calculated and expected output.

Authors - Savara Group