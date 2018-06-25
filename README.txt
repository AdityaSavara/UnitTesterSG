Using the Unit Testing Module (UnitTesterSG):

The unit tester is designed to test individual functions by storing outputs of a working function in an expected results file and comparing this output to the current output of the same function that may have been edited.
This is done so that the user can use his or her expected output to test the function at a later time to make sure the output now is the same as before and that no errors have come up.

Provided are 11 test cases in ExampleFiles: 10 have hard coded results while test11.py tests an actual function.

The template of what the test file should look like is in test11.py.  This file uses a simple function to sum values in a list together.
To use these examples, make sure UnitTesterSG.py, nestedObjectsFunctions.py, and the eleven test.py files are in the same directory.  Run UnitTesterSG and it will test all eleven cases.

You can create an expected results file ahead of time or use set_expected_results from UnitTesterSG within your test file.  This lets can hardcode the solution you expect and then compare it to the output of
your function using your input.  Initially, there will be no "expected results" to check against (unless you use set_expected_results), so after you have your function working correctly, and have verified that the output is as expected, 
you should run your function and then choose the "Y" option which will store the results.  Then, in the future, you can check against those stored results by copying the directory and replacing 
the version of your module in the fresh copy.

Using the customCompare funtion, the unit tester will work with nested objects and strings to show that the pickling worked and the object before and after pickling are the same.

Authors - Savara Group