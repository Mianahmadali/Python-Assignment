#Check if a given number is a multiple of a both 3 and 5.
def check_multiple_of_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if check_multiple_of_3_and_5(number):
    print(f"{number} is a multiple of both 3 and 5.")
else:
    print(f"{number} is NOT a multiple of both 3 and 5.")

