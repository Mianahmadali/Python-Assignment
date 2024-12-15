#Use a Boolean variable to track if a string is a palindrome without using slicing.
import re

# Get user input
input_string = input("Enter a word, phrase, or number: ")

# Clean the input: remove non-alphanumeric characters and convert to lowercase
cleaned_string = re.sub(r'[^A-Za-z0-9]', '', input_string).lower()

# Initialize a Boolean variable to track if the string is a palindrome
is_palindrome = False

# Check for palindromes based on the length of the cleaned string
if len(cleaned_string) == 0:
    is_palindrome = True  # An empty string is a palindrome
elif len(cleaned_string) == 1:
    is_palindrome = True  # A single character is a palindrome
elif len(cleaned_string) == 2:
    is_palindrome = cleaned_string[0] == cleaned_string[1]  # Compare two characters
elif len(cleaned_string) == 3:
    is_palindrome = cleaned_string[0] == cleaned_string[2]  # Compare first and last characters
elif len(cleaned_string) == 4:
    is_palindrome = cleaned_string[0] == cleaned_string[3] and cleaned_string[1] == cleaned_string[2]  # Compare outer and inner characters
elif len(cleaned_string) == 5:
    is_palindrome = cleaned_string[0] == cleaned_string[4] and cleaned_string[1] == cleaned_string[3]  # Compare outer and inner characters

# Output the result
if is_palindrome:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")

    #This answer is limited for only 5 characters because in this condition we only use conditonal statement

    import re

def is_palindrome(input_string):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = re.sub(r'[^A-Za-z0-9]', '', input_string).lower()
    
    # Initialize a Boolean variable to track if the string is a palindrome
    is_palindrome = True
    
    # Use two pointers to compare characters from both ends
    left = 0
    right = len(cleaned_string) - 1
    
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            is_palindrome = False  # Set the flag to False if characters don't match
            break  # No need to check further
        left += 1
        right -= 1
    
    return is_palindrome

# Get user input
user_input = input("Enter a word, phrase, or number: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")
