#How would you use a ternary operator to assign a value based on a condition? Write an example that checks if a number is even or odd.
num = int(input("Enter any number :"))
check_num = "even" if num % 2 == 0 else "odd"
print(check_num)