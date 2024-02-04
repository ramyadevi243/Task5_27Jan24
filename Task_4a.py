'''
Name: Ramya
Date: 29/01/2024
'''

# Problem : Write a Python function to validate the Regular Expression for Email address

# Imported re module
import re

# Defined a method to validate EmailId
def validate_email_address(email_id):
    # Left side of @ symbol can consist of any characters from lower case a to z or .
    # +@ We have to add the @ symbol
    # Right side of @ can consist of any characters from a to z of length between 2 and 6 charecters long
    pattern = "^[a-z0-9.]+@[a-z0-9]+.+[a-z]{2,6}$"
    # Searches if the pattern matches the email id and
    # returns the value in result
    result = re.search(pattern, email_id)
    # If result is true, SUCCESS message is returned
    if result:
        return "SUCCESS: Email ID is valid"
    # Else, ERROR message is returned
    else:
        return "ERROR : Invalid Email ID"

# Passing the argument to the function
email_id = "ramya83@gmail.com"

# Prints the relevant message
print(validate_email_address(email_id))
