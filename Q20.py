#Create a program that evaluates if an inputted number is prime.
num = int(input("Enter any number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"The {num} is not a prime number.")
            break
    else:
        print(f"The {num} is a prime number.")
else:
    print(f"The {num} is not a prime number.")
