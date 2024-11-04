#Write a program to check if a number is within a specified range.
num=int(input("Enter a number :"))
lower=int(input("Enter lower number :"))
upper=int(input("Enter upper number :"))
if num>lower and num<upper:
    print(f"The number {num} is within the range {lower} to {upper}.")
else:
    print(f"The number {num} is not within the range {lower} to {upper}.")