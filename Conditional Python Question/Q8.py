#Create a program that checks if a given string is palindrome.
word=str(input("Enter your any word="))
if word==word[::-1]:
    print(f"{word}  is Palindrome")
else:
    print(f"{word} is not palindrome")

