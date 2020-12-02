#setup the modules for create the random numbers
import random

nums = [random.randint(0 ,20) for i in range(10)]

def binarySearch(aList , nums):
    aList.sort()
    while aList:
        mid = len(aList)//2
        if aList[mid] == nums:
            return True
        elif aList[mid]>nums:
            aList = aList[:mid]
        elif aList[mid]<nums:
            aList = aList[mid+1:]
    return False
print(sorted(nums))
print(binarySearch(nums , 3))