#Create a Python program that checks if all elements in a list are positive using conditional statements inside a loop.
# Get user input for the list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
number_list = list(map(int, user_input.split()))

# Initialize a Boolean variable to track if all elements are positive
all_positive = True

# Loop through each number in the list
for number in number_list:
    # Check if the current number is not positive
    if number <= 0:
        all_positive = False  # Set the flag to False if any number is not positive
        break  # Exit the loop early since we found a non-positive number

# Output the result
if all_positive:
    print("All elements in the list are positive.")
else:
    print("Not all elements in the list are positive.")

