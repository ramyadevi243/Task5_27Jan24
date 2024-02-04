'''
Name: Ramya
Date: 29/01/2024
'''

# Problem : Write a Python function to validate the Regular Expression for
# Bangladesh mobile numbers

# Imported re module
import re

# Defined a method to validate Bangladesh mobile number
def validate_bangladesh_mobile_number(mobile_number):
    # 088 - country code of Bangladesh
    # 01 - Every mobile number starts with 01
    # [3-9]{8} - Mobile number can be any digit from 3 to 9 of total 8 digits
    pattern = "^[088]+[01]+[3-9]{8}$"
    # Searches if the pattern matches the mobile number and
    # returns the value in result
    result = re.search(pattern, mobile_number)
    # if result is true, then it prints SUCCESS message
    if result:
        return "SUCCESS : Bangladesh Mobile Number is Valid"
    # Else it returns ERROR message
    else:
        return "ERROR : Invalid Mobile Number"
   
# Passing the argument to the function
mobile_number = "0880135487963"

# Prints the relevant message
print(validate_bangladesh_mobile_number(mobile_number))

