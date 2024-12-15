#Use a lambda function with a conditional statement to find the larger of two numbers.
# Define the lambda function to find the larger of two numbers
larger = lambda x, y: x if x > y else y

# Test the lambda function with two numbers
num1 = 10
num2 = 20

# Use the lambda function to find the larger number
result = larger(num1, num2)

# Print the result
print("The larger number is:", result)