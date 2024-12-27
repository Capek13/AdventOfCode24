from myFunctions import MyFunctions
print("start")
data = MyFunctions.OpenFile("day1_input.txt")
col1,col2 = MyFunctions.GetNumberCollumns(data)

if type(col1) != str or type(col2) != str:
    col1.sort()
    col2.sort()
result=0

for value in col1:
    col2len = len(col2)
    halfLen = int(col2len/2)
    halfIndex = halfLen
    findIndex = -1
    findCount = 0
    OccurrenceCount = 0
    
    while halfLen > 0 and findIndex < 0:
       halfLen = int(halfLen/2)
       if col2[halfIndex] > value:
           halfIndex = halfIndex - halfLen
       elif col2[halfIndex] < value:
            halfIndex = halfIndex + halfLen
       elif col2[halfIndex] == value:
           findIndex = halfIndex
    
    if  findIndex >=0:
        lowIndex = findIndex
        highIndex = findIndex
        while col2[lowIndex-1] == value and lowIndex > 0:
            lowIndex -= 1
        while col2[highIndex+1] == value and highIndex < col2len:
            highIndex += 1
        OccurrenceCount = highIndex - lowIndex +1

    result = result + value * OccurrenceCount

print(result)
       