class MyFunctions():

    def OpenFile(fileName):
        f = open(fileName, "r")
        list = f.read().split("\n")
        return list
    
    # in must be fix for more collumns
    def GetCollumns(data):
        col1,col2 = [],[]
        collumnsCount = -1
        for value in data:
            splitedValue = value.split("   ")
            if collumnsCount < 0:
                collumnsCount = len(splitedValue)
            if len(splitedValue)== 2:
                if splitedValue[0].isnumeric() and splitedValue[1].isnumeric():
                    x,y = splitedValue
                    col1.append(int(x))
                    col2.append(int(y))
                else:
                    print("value x or y is not number")
            else:
                print(f"In line is different count of values! Expected first line value values count {0}", collumnsCount)
        return col1,col2
    
    
    def GetListsList(data):
        newData = []
        for value in data:
            splitedValues = value.split(" ")
            numbers = []
            for number in splitedValues:
                numbers.append(int(number))
            newData.append(numbers)
        return newData
