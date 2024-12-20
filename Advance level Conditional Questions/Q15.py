#Write a Python program to check if a string contains only unique characters. Use nested loops and conditional statements.
# Input string
input_string = str(input("Enter any String"))  # Change this to test with different strings

# Flag to indicate if the string has unique characters
is_unique = True

# Check for unique characters using nested loops
for i in range(len(input_string)):
    for j in range(i + 1, len(input_string)):
        if input_string[i] == input_string[j]:
            is_unique = False
            break  # Exit the inner loop if a duplicate is found
    if not is_unique:
        break  # Exit the outer loop if a duplicate is found

# Output the result
if is_unique:
    print("The string contains only unique characters.")
else:
    print("The string does not contain unique characters.")