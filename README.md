[![PyPI version](https://badge.fury.io/py/UnitTesterSG.svg)](https://badge.fury.io/py/UnitTesterSG)
[![DOI:<10.11578/dc.20200908.6>](http://img.shields.io/badge/DOI-10.11578/dc.20200908.6-green.svg)](<https://doi.org/10.11578/dc.20200908.6>) [![Build Status](https://app.travis-ci.com/AdityaSavara/UnitTesterSG.svg?branch=master)](https://app.travis-ci.com/AdityaSavara/UnitTesterSG)  [![UnitTests:<UnitTests>](http://img.shields.io/badge/UnitTests-Passing-blue.svg)](<Passing-blue>) 
[![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


# UnitTesterSG

The LICENSE and MANUAL are in the UnitTesterSG directory, and at https://github.com/AdityaSavara/UnitTesterSG/tree/master/UnitTesterSG 

# QUICK INTRO:

UnitTesterSG is for unit testing scientific/engineering outputs. It accommodates nested and even staggered array type structures, and mixed data types (like strings and integers etc). It also enables you to set numerical and absolute tolerances. Compatible with pytest.

Easiest to install by pip install UnitTesterSG, or pip install UnitTesterSG[COMPLETE]   , using the "COMPLETE" keyword will include color printing for 'passed' and 'failed' tests (https://pypi.org/project/UnitTesterSG/). After installation, to download the examples, go to https://github.com/AdityaSavara/UnitTesterSG/  --> click 'code' --> download.

To see a simple example usages, look at test_12.py and test_13.py inside the test12 and test13 directories. Normally, you'll put one or more unit test in a subdirectory (like test12 and test13).
There are three ways to run unit tests:
 **To run the test file directly, like test_12.py. This is useful when you first make a unit test.
 **To run all of your unit tests after you've made a change in your software, run pytestDriver (recommended) or UnitTesterSG (more interactive) from the parent directory of the test file by copying runPytestDriver and runUnitTesterSG into the parent directory.
    -- A typical usage is to make a directory called "unittests", to place runPytestDriver and runUnitTesterSG, and then to make subdirectories like "test1" "test2" etc.
    -- Try running runPytestDriver and runUnitTesterSG in the package to see what happens. If your test13 is fresh, it will fail the first time.
 **You can also run pytest within an individual unittest directory.

Note: For any individual test, set allowOverwrite to False when calling doTest if you want to skip UnitTesterSG from stopping to notify user when results match but result strings don't. 

# COMPATIBILITY WITH PYTEST AND TRAVIS CI:
Add a .travis.yml to your root directory, and the script command "python3 runPytestDriver.py failWithError" within it (like the one in this repository).
One advantage of this software over normal pytest usage is that UnitTesterSG does not require an __init__.py file in unit testing directories (and it is recommended not to include one).
Normally, a new pytest executable will be launched in each unit test directory.  When where there is an __init__.py file present in the directory, then pytest will be run within the same python instance.

# COMPARISON TO OTHER UNIT TESTING SOFTWARE:
UnitTesterSG is a unit testing framework that is designed for nested and/or scientific/engineering data structures. It is designed primarily for testing the outputs if a single function or simulation run by storing the expected results file such that comparisons to the stored output can be made with unit tests after the function or software has been edited. However, the compare nested objects module can also be imported directly and is quite useful even outside of unit testing.

This software is designed to be able to unit test arrays, strings, as well as nested and deeply nested objects (including arrays with tuples inside, arrays with strings inside, etc.). The software is compatable with nested objects, and thus has a dependency on the nestedObjectsFunctions module within. The software takes *calculated* results and then compares them to *expected* results. If no expected results are available (or they do not match the calculated results) the software then offers to store the calculated results as expected results for next time. Importantly, the software can also compare lists /arrays with multiple types of objects inside of them.

# EXAMPLES:
Test12 and Test13 have been made to be very easy to follow for typical usage. Thes can serve as templates of what a test file should look like during practical use.

Also provided are multiple test cases in ExampleFiles: some have hard coded results while test 11 one shows how make a test file using an external function for a simulation/processing.  Test 11 uses a simple function to sum values in a list together.

In general, test files should be named test_N.py, where N is an integer test number. Then, to run the tests, either UnitTesterSG.runUnitTests() or UnitTesterSG.pytestDriver() must be called from within the same directory as the tests, or a parent directory of the tests. With either of these commands, UnitTesterSG will run the test files contained in its directory and also in any of the direct subdirectories. This repository has two simple files, runUnitTesterSG.py and runPytestDriver.py to demonstrate usage.

When running UnitTesterSG, it will only run test files that have names like "test_1.py", "test_2.py", etc. For example, in the current structure, if runPytestDriver.py or runUnitTesterSG.py are run, they will test all of the files contained in the example subdirectories.

Essentially, there are two aspects that this module handles: Storing expected results, and comparing to previously stored expected results.

Note: For any individual test, set allowOverwrite to False when calling doTest if you want to skip UnitTesterSG from stopping to notify user when results match but strings don't. 


# STORING EXPECTED RESULTS:
Initially, there will be no "expected results" to check against. You can create an expected results file ahead of time by using the set_expected_results function.  More typically, you would first check that your function works ahead of time, manually, and then make test_1.py, test_2.py, etc. files (see examples) with interactiveTesting=True.  Then, when running UnitTesterSG you would choose the "Y" option to store the (already checked) results as the "Expected" results, when prompted. This way, they will be available for for later in the future. It is important that the function can work with "pickling" objects, which stores them in a way that they can be retrieved even after the program has ended. Thus, during running process, the module does check that it was able to properly pickle and retreive objects, by comparing whether the objects before and afer pickling are the same.


# COMPARING TO PREVIOUSLY STORED EXPECTED RESULTS:
Later, in the future, after you edit your function, you can check the revised function's outputs against those stored results by making a copy of the full subdirectory where you did the testing and replacing the version of your module in the fresh copy. Note that your (old) stored results will be in the freshly copied directory, so the unit tester will then compare your revised function's output to the stored output.

One can run pytestDriver from a root directory, and then it will use pytest for all of the UnitTesterSG tests automatically to make sure they still pass (relative to stored results).  The underscore in the file names are partially to be compatible with pytest.  So essentially one can have a UnitTests directory with subdirectories containing the unit test files for various functions, and then can place runUnitTesterSG.py or runPytestDriver.py in the main directory.

Note: For any individual test, set allowOverwrite to False when calling doTest if you want to skip UnitTesterSG from stopping to notify user when results match but strings don't. 


# TOLERANCES
The code includes the ability to use absolute and/or relative tolerances as optional arguments.  Recommended values (if they will be used) are 1E-5 for the relative tolerance, and 1E-8 for the absolute tolerance.

# RELATED PROJECTS:
https://github.com/astropy/pytest-arraydiff
https://docs.pytest.org/en/latest/reference.html
