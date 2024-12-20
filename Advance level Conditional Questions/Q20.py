# Advanced Problem-Solving
# Write a Python program that accepts a date (day, month, year) and determines whether the date is valid. Handle leap years and invalid months/days.\
# Get user input
# Get user input for day, month, and year
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# Initialize a variable to check if the date is valid
is_valid_date = True

# Check if the month is valid
if month < 1 or month > 12:
    is_valid_date = False
    print("Invalid month! Please enter a month between 1 and 12.")
else:
    # Check for the number of days in the month
    if month in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
        max_days = 31
    elif month in [4, 6, 9, 11]:  # Months with 30 days
        max_days = 30
    else:  # February
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_days = 29  # Leap year
        else:
            max_days = 28  # Non-leap year

    # Check if the day is valid
    if day < 1 or day > max_days:
        is_valid_date = False
        print(f"Invalid day! Please enter a day between 1 and {max_days} for month {month}.")

# Final output
if is_valid_date:
    print(f"The date {day}-{month}-{year} is valid.")
else:
    print("The date entered is not valid.")
