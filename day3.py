from myFunctions import MyFunctions
import re
print("start")
data = MyFunctions.OpenFile("day3_input.txt")
result = 0 # result
text="".join(data)

text= text.replace(" ","")

values = re.findall(r"mul\(\b([0-9]|[1-9][0-9]{1,2})\b,\b([0-9]|[1-9][0-9]{1,2})\b\)",text)
print(values)
myList = map(lambda x,y: int(x)*int(y), values)
print(list(myList))