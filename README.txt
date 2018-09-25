Using the Unit Testing Module (UnitTesterSG, version 4.0 as of aug 3rd 2018):

PURPOSE OF MODULE:
The unit tester is designed to test individual functions by storing outputs of a working function in an expected results file and comparing this output to the current output of the same function that may have been edited.
This is done so that the user can use his or her expected output to test the function at a later time to make sure the output now is the same as before and that no errors have come up. This module is designed to be able to unit test arrays, strings, as well as nested and deeply nested objects (including arrays with tuples inside, arrays with strings inside, etc.). The module is compatable with nested objects, and thus has a dependency on the nestedObjectsFunctions module. The module takes *calculated* results and then compares them to *expected* results. If no expected results are available (or they do not match the calculated results) the module then offers to store the calculated results as expected results for next time.

EXAMPLES:
Provided are multiple test cases in ExampleFiles: some have hard coded results while the last one shows how to use write a test file using a function.

A typical template of what a test file should look like during practical use is in test_11.py.  This file uses a simple function to sum values in a list together.
To use these examples, make sure UnitTesterSG.py, nestedObjectsFunctions.py, and the testN.py files, where N is an integer test number, are in the same directory.  The test files should be in the same directory or in the direct subdirectories.  UnitTesterSG will run the test files contained in its directory and also in any of the direct subdirectories. When running UnitTesterSG, it will only run test files that have names like "test_1.py", "test_2.py", etc. For example, in the current structure, if UnitTesterSG is run, it will test all of the files contained in the example file directory.

Essentially, there are two aspects that this module handles: Storing expected results, and comparing to previously stored expected results.

STORING EXPECTED RESULTS:
Initially, there will be no "expected results" to check against. You can create an expected results file ahead of time by using the set_expected_results function.  More typically, you would first check that your function works ahead of time, manually, and then make test_1.py, test_2.py, etc. files (see examples).  Then, when running UnitTesterSG you would choose the "Y" option to store the (already checked) results as the "Expected" results, when prompted. This way, they will be available for for later in the future. It is important that the function can work with "pickling" objects, which stores them in a way that they can be retrieved even after the program has ended. Thus, during running process, the module does check that it was able to properly pickle and retreive objects, by comparing whether the objects before and afer pickling are the same.


COMPARING TO PREVIOUSLY STORED EXPECTED RESULTS:
Later, in the future, after you edit your function, you can check the revised function's outputs against those stored results by making a copy of the full subdirectory where you did the testing and replacing the version of your module in the fresh copy. Note that your (old) stored results will be in the freshly copied directory, so the unit tester will then compare your revised function's output to the stored output.

One can run pytest from a root directory, and then pytest will run all of the UnitTesterSG tests automatically to make sure they still pass (relative to stored results).  The underscore in the file names are partially to be compatible with pytest. The pytestDriver.py file will run pytest on each subdirectory of the directory pytestDriver.py is in.  So essentially one can have a UnitTests directory with subdirectories containing the unit test files for various functions so runnnig the pytest driver runs pytest on each test file in the UnitTests directory.

TOLERANCES
We have added the ability to use absolute and relative tolerances as optional arguments.  Recommended values (if they will be used) are 1E-5 for the relative tolerance, and 1E-8 for the absolute tolerance.
Authors - Savara Group
