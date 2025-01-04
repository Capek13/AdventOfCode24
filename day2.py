from myFunctions import MyFunctions
print("start")
data = MyFunctions.OpenFile("day2_input.txt")
#data = MyFunctions.OpenFile("day2_dataSample.txt")
data = MyFunctions.GetListsList(data)
safeCount = 0 # result

def CompareDifference(value1, value2):
    if 0 < abs(value1 - value2) < 4 :
        return 1
    else:
        return 0


def CheckSteps(value0,value1,value2):
    if value0 - value1 > 0 and value1 - value2 > 0:
        return 1
    elif value0 - value1 < 0 and value1 - value2 < 0:
        return 1
    else:
        return 0

def ForeachValues(values,toleranceNotUsed):
    lastIndex = len(values)-1
    for i in range(0, lastIndex):
                ii = i+1
                if CompareDifference(values[i],values[ii]) == False:
                    if toleranceNotUsed:
                        if ForeachValues(values[:ii]+values[ii+1:],False):
                            return 1
                        else:
                            return ForeachValues(values[:i]+values[i+1:],False)
                    else:
                        return 0
                if i > 0:            
                    if CheckSteps(values[i-1],values[i],values[ii])==False:
                        if toleranceNotUsed:
                            if ForeachValues(values[:ii]+values[ii+1:],False):
                                return 1
                            else:
                                if ForeachValues(values[:i]+values[i+1:],False):
                                    return 1
                                else:
                                    return ForeachValues(values[:i-1]+values[i:],False)
                        else:           
                            return 0
                if i == lastIndex-1:
                    return 1
                
for values in data:
    toleranceNotUsed = True # For 1part change this value to False
    safeCount += ForeachValues(values,toleranceNotUsed)
        
print(f"Save reports was found: {safeCount}")
