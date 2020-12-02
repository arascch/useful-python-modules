def insertionSort(fList):
    for i in range(1 , len(fList)):
        if fList[i]<fList[i-1]:
            for j in range(i , 0 , -1):
                if fList[j]<fList[j-1]:
                    fList[j] , fList[j+1]=fList[j+1] , fList[j]
        else:
            break
    
    return fList