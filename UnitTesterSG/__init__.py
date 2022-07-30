from UnitTesterSG.UnitTesterSGFunctions import *

def pytestDriver(failWithError=False):
    import UnitTesterSG.pytestDriver
    pytestDriver.runAllTests(failWithError=failWithError)

def runUnitTests():
    import UnitTesterSG.UnitTesterSGFunctions
    UnitTesterSG.UnitTesterSGFunctions.runAllTests()

def main():
    import UnitTesterSG.UnitTesterSGFunctions
    UnitTesterSG.UnitTesterSGFunctions.runAllTests()

if __name__=="__main__":
    import UnitTesterSG.UnitTesterSGFunctions
    UnitTesterSG.UnitTesterSGFunctions.runAllTests()