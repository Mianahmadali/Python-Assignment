# Custom Conditional Functions
# Write a custom Python function that takes three arguments (low, high, value) and returns True if the value lies between low and high, using conditional
# Define the low, high, and value
low = int(input("Enter low value :"))
high = int(input("Enter high value :"))
value = int(input("Enter Value which you want to check :")) # Change this value to test with different numbers

# Check if the value lies between low and high using conditional statements
if low < value < high:
    result = True
else:
    result = False

# Output the result
if result:
    print(f"The value {value} lies between {low} and {high}.")
else:
    print(f"The value {value} does not lie between {low} and {high}.")