# 87-Python Program that validates given mobile number. Number should start with 7, 8 or 9 
# followed by 9 digits. 

import re

def validate_mobile_number(number):
    pattern = r"^[7-9]\d{9}$"
    if re.match(pattern, number):
        return True
    else:
        return False

# Test cases
numbers = ["1234567890", "9876543210", "7654321098", "6543210987", "9123456780"]

for number in numbers:
    if validate_mobile_number(number):
        print(number, "is a valid mobile number.")
    else:
        print(number, "is not a valid mobile number.")