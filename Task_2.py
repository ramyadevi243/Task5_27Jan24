'''
Name: Ramya
Date: 29/01/2024
'''

# Write a Python code using Lambda function to check every element of a List is
# an Integer or String

# Created a list
list_of_data = ["notebook", "Chennai", 3, "python", 567, "January", "56#$"]

# Created a function using lambda to check if every element is a string or integer
is_integer_or__string = lambda x : isinstance(x, (int, str))

# Created a variable called result to store the return value of function
result = all(list(map(is_integer_or__string, list_of_data)))

# using conditional statement, print the result True if elements in list
# is integer or string
if result == True:
    print("All elements of the list is integer or string")
else:
    print("Not all elements of the list is integer or string")