#setup the modules for create the random numbers
import random

nums = [random.randint(0 ,20) for i in range(10)]

print(sorted(nums))