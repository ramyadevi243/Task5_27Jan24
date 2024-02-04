'''
Name: Ramya
Date: 29/01/2024
'''

# Problem : Write a Python function to validate the Regular Expression for a password

# Imported re module
import re

# Defined a method to validate password
def validate_password(password):
    # Password should consist of 16 characters
    # Alpha-numeric with alphabets of Upper case, Lower case, Special Characters, Numbers
    pattern = "^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])(?=.*[!@#$%^&*]).{16}$"
    # Searches if the pattern matches the password and
    # returns the value in result
    result = re.search(pattern, password)
    # If result is true, SUCCESS message is returned
    if result:
        return "SUCCESS: Password is accepted"
    # Else, ERROR message is returned
    else:
        return "Invalid password"

# Passing the argument to the function
password = "SramyaDevi123!@#"

# Prints the relevant message
print(validate_password(password))