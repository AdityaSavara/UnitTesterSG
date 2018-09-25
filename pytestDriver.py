import os

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
        os.system("del __pycache__ /Q")
    except:
        pass
    os.system("pytest")
    os.chdir("..")
