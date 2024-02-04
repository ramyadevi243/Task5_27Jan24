'''
Name: Ramya
Date: 29/01/2024
'''

# Using Python lambda function, create a Fibonacci series from 1 to 50 elements.

# Import reduce module
from functools import reduce

# Number of elements 50 elements
n = 50

# Creating a Fibonacci series, starting from 1 up to 50 elements
# Used reduce function to perform operation cumulatively to the items in range
fibonacci_series = reduce(lambda x, _: x + [x[-1] + x[-2]], range(2, n), [1, 1])

print("Fibonacci series from 1 up to 50 elements: ", fibonacci_series)