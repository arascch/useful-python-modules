
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
#for calculate the number in your mind you can change the below number
print(fib(10))