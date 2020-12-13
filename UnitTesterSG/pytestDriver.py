import os
import sys

def runAllTests():
    #in Python, the listdir command  returns files and directories (like typeing in "dir").
    listOfDirectoriesAndFiles = os.listdir(".")

    #Below is going to become a list of directories only in the next loop.
    directoryList = []
    for elem in listOfDirectoriesAndFiles:
        if os.path.isdir(elem) == True:
            directoryList.append(elem)

    #This loop goes into each directories, runs the specified command, and comes back.
    for directory in directoryList:
        print("Changing directory to "+directory)
        os.chdir(directory)
        try:
            os.system("del __pycache__ /Q") #for windows
            os.system("rm __pycache__ /Q") #for linux
        except:
            pass
        os.system(sys.executable +" -m pytest") #this is like typing "python -m pytest" but uses whichever version of python should be used, important for virtual environments and different systems https://stackoverflow.com/questions/8338854/how-to-run-py-test-against-different-versions-of-python
        os.chdir("..")