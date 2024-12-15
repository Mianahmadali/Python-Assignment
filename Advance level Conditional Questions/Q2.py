#Write a program that determines if a number is divisible by 3, 5, or both. Use nested conditional statements for this.
# Get user input for a number
number = int(input("Enter a number: "))

# Check divisibility using nested conditional statements
if number % 3 == 0:
    if number % 5 == 0:
        print("The number is divisible by both 3 and 5.")
    else:
        print("The number is divisible by 3.")
else:
    if number % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("The number is not divisible by 3 or 5.")