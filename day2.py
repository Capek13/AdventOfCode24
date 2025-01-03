from myFunctions import MyFunctions
print("start")
data = MyFunctions.OpenFile("day2_input.txt")
data = MyFunctions.GetListsList(data)
safeCount = 0 # result

for values in data:
    state = ""
    if len(values) > 1:
        if values[0]-values[1] > 0:
            state = "decreasing"
        elif values[0]-values[1] < 0:
            state = "increasing"
        else:
            continue

        lastIndex = len(values)-1
        for i in range(0, lastIndex):
            difference = abs(values[i] - values[i+1])
            if difference > 3 or difference == 0 :
                break

            if state == "decreasing":
                if values[i]-values[i+1] < 0:
                    break
            elif state == "increasing":
                if values[i]-values[i+1] > 0:
                    break

            if i == lastIndex-1:
                safeCount += 1

print(f"Save reports was found: {safeCount}")
