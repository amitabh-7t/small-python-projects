#5. Implement a Python program to determine the factorial of a number provided by the user.
fact = int(input("enter number : "))

def factorial(fn):
    if fn == 0:
        return 1
    else:
        return (fn * factorial(fn-1))
    

    
print(factorial(fact))