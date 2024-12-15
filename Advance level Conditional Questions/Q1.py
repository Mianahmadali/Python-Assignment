#How do you combine multiple conditions using logical operators (and, or, not) in a Python if statement? Provide an example.
num = int(input("Enter any number: "))

if num >= 90 and num <= 100:
    print("Number is between 90 and 100")
elif num >= 80 and num < 90:
    print("Number is between 80 and 90")
elif num >= 70 and num < 80:
    print("Number is between 70 and 80")
else:
    print("The number is less than 70")




    age = int(input("Enter your age: "))
has_access_pass = input("Do you have a valid access pass? (yes/no): ").strip().lower()

# Check if the user is not allowed to access the restricted area
if not (age >= 18 and has_access_pass == 'yes'):
    print("Access denied. You must be at least 18 years old and have a valid access pass.")
else:
    print("Access granted. Welcome!")

# Get user input for age and membership status
age = int(input("Enter your age: "))
is_member = input("Are you a member of the store? (yes/no): ").strip().lower()

# Check eligibility for discount
if (age < 18 or age > 65) or not (is_member == 'yes'):
    print("You are eligible for a special discount!")
else:
    print("You are not eligible for a special discount.")