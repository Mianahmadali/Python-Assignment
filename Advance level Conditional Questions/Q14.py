#Explain how short-circuit evaluation works in Python's conditional statements with an example.
# Variables for demonstration
a = 5
b = 10
c = 15

# Using 'and' with short-circuit evaluation
if a < b and b < c:
    print("Both conditions are True: a is less than b and b is less than c.")
else:
    print("At least one condition is False.")

# Changing the value of 'a' to demonstrate short-circuiting
a = 20
if a < b and b < c:
    print("Both conditions are True: a is less than b and b is less than c.")
else:
    print("At least one condition is False.")

# Using 'or' with short-circuit evaluation
if a < b or b < c:
    print("At least one condition is True: a is less than b or b is less than c.")
else:
    print("Both conditions are False.")

# Changing the value of 'b' to demonstrate short-circuiting
b = 25
if a < b or b < c:
    print("At least one condition is True: a is less than b or b is less than c.")
else:
    print("Both conditions are False.")

#This is called short circuit evalution
