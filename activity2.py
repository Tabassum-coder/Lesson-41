#Factorial

def fact(n):
    if n==1:
       return n
    else:
        return n*fact(n-1)

num=int(input("Enter a num"))

if num<0:
    print("Cannot find factorial for numbers less than 0")
elif num==0:
    print("Factorial is 1")
else:
    print("Factorial of ",num," is ",fact(num))