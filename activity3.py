#Calculator
def add(a,b):
    return a+b

def diff(a,b):
    return a-b

def prod(a,b):
    return a*b

def quotient(a,b):
    return a//b

n1=int(input("Enter first number"))
n2=int(input("Enter second number"))


print("Sum of {0} and {1} is {2}".format(n1,n2,add(n1,n2)))
print("Difference of {0} and {1} is {2}".format(n1,n2,diff(n1,n2)))
print("Product of {0} and {1} is {2}".format(n1,n2,prod(n1,n2)))
print("Quotient of {0} and {1} is {2}".format(n1,n2,quotient(n1,n2)))