import os
import sys

def runAllTests(failWithError=False):
    #in Python, the listdir command  returns files and directories (like typeing in "dir").
    listOfDirectoriesAndFiles = os.listdir(".")

    #Below is going to become a list of directories only in the next loop.
    directoryList = []
    for elem in listOfDirectoriesAndFiles:
        if os.path.isdir(elem) == True:
            directoryList.append(elem)
 
    allTestsPassed = True #initializing a flag to check if all tests have passed. Will change to False if any tests fail.
    #This loop goes into each directories, runs the specified command, and comes back.
    for directory in directoryList:
        print("Changing directory to "+directory)
        os.chdir(directory)
        
        try:
            os.system("del __pycache__ /Q") #for windows
            os.system("rm -r __pycache__ /Q") #for linux
        except:
            pass
        
        #We will check if __init__ exists, because for various situations, pytest.main( will have failures if there is no __init__.
        initExists = os.path.exists('__init__.py')
        if initExists:        
            #Try to run the test. In the past, we we used an executable version of pytest, but now we are using "pytest.main()" so we can get the exit code, that way we can fail with error if a unit test doesn't pass.
            import pytest
            #before running pytest, add the current working directory.
            currentTestDirectory = os.curdir #keep the directory in a variable because we will remove them again at the end.
            sys.path.insert(0, currentTestDirectory)
            exitCode = pytest.main()
            # https://stackoverflow.com/questions/8338854/how-to-run-py-test-against-different-versions-of-python
            if exitCode >= 1 and exitCode <5:
                allTestsPassed = False
            #now remove the current directory.
            sys.path.remove(currentTestDirectory)
        else: #if __init__ does not exist, we can usually still run the unit tests by running the pytest executable.
            os.system(sys.executable +" -m pytest") #this is like typing "python -m pytest" but uses whichever version of python should be used, important for virtual environments and different systems
        os.chdir("..")
    
    if allTestsPassed == False:
        print("At least one unit test failed.")
        if failWithError == True: #if the failWithError flag is on due to the optional argument, we will check if all tests passed. If not, we'll raise an error.
            raise RuntimeError("At least one unit test failed.")  #This is to intentionally create an error so that the Travis CI will fail.