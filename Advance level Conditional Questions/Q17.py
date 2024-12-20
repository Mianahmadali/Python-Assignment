# Chained Comparisons
# Use chained comparisons in a conditional statement to determine if a number lies between two values.
# Define the number to check
number = 15  # Change this value to test with different numbers

# Define the range
lower_bound = 10
upper_bound = 20

# Use chained comparisons to check if the number is between the two values
if lower_bound < number < upper_bound:
    print(f"The number {number} lies between {lower_bound} and {upper_bound}.")
else:
    print(f"The number {number} does not lie between {lower_bound} and {upper_bound}.")