#9. Design a Python program to swap two numbers without using a temporary variable.
def swap1(a,b):
    a=b
    return a
def swap2(a,b):
    b=a
    return b
a = int(input("a= "))
b = int(input("b= "))
print(swap1(a,b),swap2(a,b))