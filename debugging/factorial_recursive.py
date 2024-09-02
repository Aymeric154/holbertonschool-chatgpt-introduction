#!/usr/bin/python3

import sys  # Import the sys module to handle command-line arguments

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the integer n.
    """
    if n == 0:
        # Base case: the factorial of 0 is defined as 1
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Convert the first command-line argument to an integer and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the result to the console
print(f)