# 11. Write a Python program to generate the Fibonacci sequence up to a specified number of terms.
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    count = 0
    while count < n:
        fib_sequence.append(a)
        a, b = b, a + b
        count += 1
    return fib_sequence

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence up to", n, "terms:")
    print(fibonacci(n))
