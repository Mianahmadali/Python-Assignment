#Write a program that asks for an integer and checks if its divisible by 2,3 or both.
num=int(input("Enter any number:"))
if num%2==0 and num%3==0:
    print(f"the {num} is divisible by both 2,3")
elif num % 2==0:
    print(f"the {num} is divisible by 2")
elif num % 3== 0:
    print(f"the {num} is divisible by 3")   
else:
    print(f"the {num} is not divisible by both 2,3")