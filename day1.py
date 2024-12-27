from myFunctions import MyFunctions
print("start")
data = MyFunctions.OpenFile("day1_input.txt")
col1,col2 = MyFunctions.GetNumberCollumns(data)

if type(col1) != str or type(col2) != str:
    col1.sort()
    col2.sort()
result=0
for i in range(0,len(col1)):
    result = result + abs(col2[i]-col1[i]) 
print(result)