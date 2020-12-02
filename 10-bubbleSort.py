#the function for bubble sort
def bubbleSort(fList):
    for i in range(len(fList)):
        switch = False
        for j in range(len(fList)-1):
            if fList[j]>fList[j+1]:
                fList , fList[j+1] = fList[j+1] , fList[j]
                switch = True
        if switch == False:
            break
    return fList