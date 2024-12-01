#Check if a year input bt the users is a century year.
year=int(input("Enter any year :"))
if year % 100==0:
    print(f"The {year} is century year")
else:
    print(f"the {year} is not a century year")