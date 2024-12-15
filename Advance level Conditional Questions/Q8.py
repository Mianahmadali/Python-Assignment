#Implement a nested if-else statement to validate a password:

"""Check if it has at least 8 characters.
Check if it contains a number.
Check if it contains a special character (e.g., @, #, $, etc.).
"""
import re  # Importing the regular expression module ------------

password = input("Enter a Password: ")

# Check if the password has at least 8 characters
if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    # Check if the password contains at least one number
    if re.search(r'\d', password):
        # Check if the password contains at least one special character-------------
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("Password is valid.")
        else:
            print("Password must contain at least one special character.")
    else:
        print("Password must contain at least one number.")