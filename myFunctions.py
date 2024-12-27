class MyFunctions():

    def OpenFile(fileName):
        f = open(fileName, "r")
        list = f.read().split("\n")
        return list
    
