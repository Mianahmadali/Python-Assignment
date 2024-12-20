# Error Handling in Conditionals
# Write a Python program that checks user input for a valid integer. If the input is invalid, provide a message using conditional statements.

# Get user input
user_input = input("Please enter an integer: ")

# Check if the input is a valid integer
if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    print(f"You entered a valid integer: {user_input}")
else:
    print("Invalid input! Please enter a valid integer.")