# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/22/2024
# Define a function named fib that takes a positive integer parameter and returns the number at that position
# of the Fibonacci sequence.

# Define Fibonacci as fib
def fib(n):
    a = 0
    b = 1
# Create the loop for the Fibonacci sequence
    if n < 0:
        print ("Incorrect Input")
    elif n == 0:
        return a
    elif n == 1:
        return b
# Loop a function that follows the sequence
    else:
        while n > 1:
            c = a + b
            a = b
            b = c
            n = n - 1
# Return the number to the position of the Fibonacci sequence
        return b
