#fibonacci series using functions and for loop
def fibonacci(n):
    a=0
    b=1
    l=[]
    for i in range(n+1):
        c=a+b
        l.append(a)
        a=b
        b=c
    return l
#main code
n = int(input("enter any number"))
print("Fibonacci series is:")
fibonacci(n)
