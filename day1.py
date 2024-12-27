from myFunctions import MyFunctions
print("start")
data = MyFunctions.OpenFile("day1_input.txt")
col1,col2 = [],[]
for value in data:
    splitedValue = value.split("   ")
    if len(splitedValue)== 2:
        if splitedValue[0].isnumeric() and splitedValue[1].isnumeric():
            x,y = splitedValue
            col1.append(x)
            col2.append(y)
        else:
            print("value x or y is not number")
    else:
        print("In line is different count of values! Expected 2 values")
if type(col1) != str or type(col2) != str:
    col1.sort()
    col2.sort()


