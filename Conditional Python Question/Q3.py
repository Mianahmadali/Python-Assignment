#Write a program that checks if a given year is a leap year.
year=int(input("enter a leap year"))
if year % 4 and year % 400: 
    print("The year is leap year") 
elif year % 100:
    print("The year is not a leap year")
