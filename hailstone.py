# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/22/2024
# Define a function named hailstone that takes positive integer parameter as the initial number of
# a hailstone sequence and returns how many steps it takes to reach 1

# Define hailstone sequence as h
def hailstone(h):
    # starting the step count
    steps = 0

    #Loop until h becomes 1
    while h !=1:
    # If h is even
        if h % 2 == 0:
            h = h // 2
    # if h is odd
        else:
            h = 3 * h + 1
    # Increments of each step count
        steps += 1
# Return the number of steps
    return steps
# Run
h = int(input("Enter a positive integer"))