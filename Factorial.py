def factorial(n):
    f=1
    for i in range (1,n+1):
        f= f*i
    return f
x=int(input("enter the number"))
result= factorial(x)
print(result)

# using recursion

def factorials(n):
    if n==0 or n==1 :
        return 1
    else:
        return n * factorials(n-1)
    
y=int(input("enter the number y"))
result= factorials(y)
print(result)
