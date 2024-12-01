#Use a loop to count the number of digits in an integer.
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10  
        count += 1
    return count
number = int(input("Enter an integer: "))
print(f"The number of digits is: {count_digits(number)}")
