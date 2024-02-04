'''
Name: Ramya
Date: 29/01/2024
'''

# Problem : Write a Python function to validate the Regular Expression for
# Telephone numbers of USA

# Imported re module
import re

# Defined a method to validate telephone numbers of USA
def validate_usa_telephone_number(telephone_number):
    # USA telephone number starts with 3-digit area code
    # followed by 7-digit telephone number
    pattern = "^[0-9]{3}+[0-9]{7}$"
    # Searches if the pattern matches the telephone number and
    # returns the value in result
    result = re.search(pattern, telephone_number)
    # if result is true, then it prints SUCCESS message
    if result:
        return "SUCCESS : USA Telephone Number is Valid"
    # Else it returns ERROR message
    else:
        return "ERROR : Invalid Telephone Number"
   
# Passing the argument to the function
telephone_number = "2235879341"

# Prints the relevant message
print(validate_usa_telephone_number(telephone_number))