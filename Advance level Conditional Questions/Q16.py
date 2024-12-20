# How do you avoid comparing None in conditional statements? Provide an example.
"""The question "How do you avoid comparing None in conditional statements?" refers to the practice of ensuring that you do not inadvertently compare a variable that may be None (the Python equivalent of null) in a way that could lead to unexpected behavior or errors.

Why Avoid Comparing None?
Type Errors: If you try to perform operations or comparisons on None that are meant for other data types (like strings, integers, etc.), you may encounter TypeError.
Logical Errors: Comparing None with other values can lead to logical errors in your program, as None is a distinct type that represents the absence of a value.
How to Avoid Comparing None
Explicit Checks: Before performing comparisons, explicitly check if the variable is None.
Use Default Values: Assign default values to variables to ensure they are not None.
Use is for Comparison: When checking if a variable is None, use the is operator instead of ==, as it is more explicit and avoids potential issues with custom equality methods."""
# Example variable that may be None
value = None

# Explicit check for None before comparison
if value is not None:
    if value > 10:
        print("Value is greater than 10.")
    else:
        print("Value is 10 or less.")
else:
    print("Value is None, cannot compare.")

"""    Explanation of the Example
Initialization: The variable value is initialized to None.
Explicit Check: The first if statement checks if value is not None using is not None. This ensures that we only proceed to compare value if it has a valid value.
Comparison: If value is not None, we then safely compare it to 10.
Handling None: If value is None, the program prints a message indicating that it cannot perform the comparison.
Summary
By explicitly checking for None before performing comparisons, you can avoid errors and ensure that your code behaves as expected. This practice leads to more robust and maintainable code, especially in scenarios where variables may not always hold valid values."""