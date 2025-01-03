from myFunctions import MyFunctions
print("start")
data = MyFunctions.OpenFile("day2_input.txt")
data = MyFunctions.GetListsList(data)
safeCount = 0 # result

def CompareDifference(value1, value2):
    difference = abs(value1 - value2)
    if difference > 3 or difference == 0 :
        return False
    return True


def CheckSteps(value1,value2,state):
    if state == "decreasing":
        if value1 - value2 > 0:
            return True
    elif state == "increasing":
        if value1 - value2 < 0:
            return True
    return False

def ForeachValues(values,toleranceNotUsed):
    state = ""
    if toleranceNotUsed == False:
        print(values)
    if len(values) > 1:
        if values[0]-values[1] > 0:
            state = "decreasing"
        elif values[0]-values[1] < 0:
            state = "increasing"
        else:
            if toleranceNotUsed:
                print(values , " CHECK 1")
                return ForeachValues(values[1:],False)
            else:
                return 0
        
    lastIndex = len(values)-1
    for i in range(0, lastIndex):
                ii = i+1
                if CompareDifference(values[i],values[ii]) == False:
                    if toleranceNotUsed:
                        print(values, " COMPARE 2")
                        if i == lastIndex-1:
                            return 1
                        else:
                            if ForeachValues(values[:ii]+values[ii+1:],False):
                                return 1
                            else:
                                if ForeachValues(values[:i]+values[i+1:],False):
                                    return 1
                                else:
                                    if i > 0:
                                        print(i, "i")
                                        return ForeachValues(values[:i-1]+values[i:],False)
                    else:
                        return 0
                            
                if CheckSteps(values[i],values[ii],state)==False:
                    if toleranceNotUsed:
                        print(values , "CHECK 3")
                        if i == lastIndex-1:
                            return 1
                        else:
                            if ForeachValues(values[:ii]+values[ii+1:],False):
                                return 1
                            else:
                                if ForeachValues(values[:i]+values[i+1:],False):
                                    return 1
                                else:
                                    if i > 0:
                                        if ForeachValues(values[:i-1]+values[i:],False):
                                            return 1
                                        else:
                                            if i==2:
                                                return ForeachValues(values[1:],False)
                                            else:
                                                return 0
                                    else:
                                        return 0
                    else:           
                        return 0

                if i == lastIndex-1:
                    if toleranceNotUsed == False:
                        print("END")
                    return 1


for values in data:
    toleranceNotUsed = True
    #safeCount += ForeachValues(values,toleranceNotUsed)
    result = ForeachValues(values,toleranceNotUsed)
    safeCount += result
    #if result:
       # print(values)
        
        

print(f"Save reports was found: {safeCount}")
