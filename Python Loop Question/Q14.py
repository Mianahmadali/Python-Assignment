#Write a program that breaks the loop when a certain condition is met.
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # Break the loop when the condition is met
    else:
        print(f"You entered: {user_input}")



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 5:
        print("Found 5! Breaking the loop.")
        break  # Break the loop when the condition is met
    print(f"Current number: {number}")


count = 0

while count < 10:
    print(f"Count is: {count}")
    count += 1
    if count == 5:
        print("Count reached 5! Breaking the loop.")
        break  # Break the loop when the condition is met    