UnitTesterSG, version 5.0 as of Apr 13 2020

PURPOSE OF MODULE:
UnitTesterSG is a unit testing framework that is designed for nested and/or scientific/engineering data structures. It is designed primarily for testing the outputs if a single function or simulation run by storing the expected results file such that comparisons to the stored output can be made with unit tests after the function or software has been edited. However, the compare nested objects module can also be imported directly and is quite useful even outside of unit testing.

This software is designed to be able to unit test arrays, strings, as well as nested and deeply nested objects (including arrays with tuples inside, arrays with strings inside, etc.). The software is compatable with nested objects, and thus has a dependency on the nestedObjectsFunctions module within. The software takes *calculated* results and then compares them to *expected* results. If no expected results are available (or they do not match the calculated results) the software then offers to store the calculated results as expected results for next time. Importantly, the software can also compare lists /arrays with multiple types of objects inside of them.

EXAMPLES:
Provided are multiple test cases in ExampleFiles: some have hard coded results while test 11 one shows how make a test file using an external function for a simulation/processing.

A typical template of what a test file should look like during practical use is in test_11.py.  This file uses a simple function to sum values in a list together.

In general, test files should be named test_N.py, where N is an integer test number. Then, to run the tests, either UnitTesterSG.runUnitTests() or UnitTesterSG.pytestDriver() must be called from within the same directory as the tests, or a parent directory of the tests. With either of these commands, UnitTesterSG will run the test files contained in its directory and also in any of the direct subdirectories. This repository has two simple files, runUnitTesterSG.py and runPytestDriver.py to demonstrate usage.

When running UnitTesterSG, it will only run test files that have names like "test_1.py", "test_2.py", etc. For example, in the current structure, if runPytestDriver.py or runUnitTesterSG.py are run, they will test all of the files contained in the example subdirectories.

Essentially, there are two aspects that this module handles: Storing expected results, and comparing to previously stored expected results.

STORING EXPECTED RESULTS:
Initially, there will be no "expected results" to check against. You can create an expected results file ahead of time by using the set_expected_results function.  More typically, you would first check that your function works ahead of time, manually, and then make test_1.py, test_2.py, etc. files (see examples).  Then, when running UnitTesterSG you would choose the "Y" option to store the (already checked) results as the "Expected" results, when prompted. This way, they will be available for for later in the future. It is important that the function can work with "pickling" objects, which stores them in a way that they can be retrieved even after the program has ended. Thus, during running process, the module does check that it was able to properly pickle and retreive objects, by comparing whether the objects before and afer pickling are the same.


COMPARING TO PREVIOUSLY STORED EXPECTED RESULTS:
Later, in the future, after you edit your function, you can check the revised function's outputs against those stored results by making a copy of the full subdirectory where you did the testing and replacing the version of your module in the fresh copy. Note that your (old) stored results will be in the freshly copied directory, so the unit tester will then compare your revised function's output to the stored output.

One can run pytestDriver from a root directory, and then it will use pytest for all of the UnitTesterSG tests automatically to make sure they still pass (relative to stored results).  The underscore in the file names are partially to be compatible with pytest.  So essentially one can have a UnitTests directory with subdirectories containing the unit test files for various functions, and then can place runUnitTesterSG.py or runPytestDriver.py for running at that time.

TOLERANCES
The code includes the ability to use absolute and/or relative tolerances as optional arguments.  Recommended values (if they will be used) are 1E-5 for the relative tolerance, and 1E-8 for the absolute tolerance.
