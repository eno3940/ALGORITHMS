def Fibonacci(n):
    result =1
    if n>=2:
        result = Fibonacci(n-1)+Fibonacci(n-2)
    if n==0:
        result=0
    if n==1:
        result=1
    return result

print(Fibonacci(10))