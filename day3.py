from myFunctions import MyFunctions
import re
print("start")
data = MyFunctions.OpenFile("day3_input.txt")
result = 0 # result
text="".join(data)
text= text.replace(" ","")
values = re.findall(r"mul\(\b([0-9]|[1-9][0-9]{1,2})\b,\b([0-9]|[1-9][0-9]{1,2})\b\)",text)
myList = list(map(lambda pair: int(pair[0])*int(pair[1]), values))
print(sum(myList))
# PART 2
mulValues = list(re.finditer(r"mul\(\b([0-9]|[1-9][0-9]{1,2})\b,\b([0-9]|[1-9][0-9]{1,2})\b\)",text))
doValues = list(re.finditer(r"do\(\)",text))
dontValues = list(re.finditer(r"don't\(\)",text))

startIndex = 0
iDo=0
iDont=0 
activIntervals = []

while iDo < len(doValues)-1 or iDont < len(dontValues)-1:
    if doValues[iDo].start() < dontValues[iDont].start():
        if startIndex < 0:
            startIndex = doValues[iDo].start()
        if iDo < len(doValues)-1:
            iDo += 1
    else:    
        if startIndex >= 0:
            activIntervals.append([startIndex,dontValues[iDont].start()])
            startIndex = -1
        if iDont < len(dontValues)-1:
            iDont += 1

if doValues[-1].start() > dontValues[-1].start():
        activIntervals.append([doValues[-1].start(),-1])

myMulValues = []
for value in mulValues:
    for i in range(0,len(activIntervals)):
        if activIntervals[i][0] < value.start() < activIntervals[i][1] or activIntervals[i][1] == -1 and activIntervals[i][0] < value.start():
            myMulValues.append(value.group())
            break

myMulValues = "".join(myMulValues)
mulValues = re.findall(r"mul\(\b([0-9]|[1-9][0-9]{1,2})\b,\b([0-9]|[1-9][0-9]{1,2})\b\)",myMulValues)
myList = list(map(lambda pair: int(pair[0])*int(pair[1]), mulValues))

print(sum(myList))
