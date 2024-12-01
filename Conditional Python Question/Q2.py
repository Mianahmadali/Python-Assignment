#Take a user's age as a input and display weather they are a minor,adult, or senior citizens.
age=int(input("Enter Your age"))
if age>=18 and age<50 :
    print("The users is adult")
elif age<18:
    print("The users is minor")    
else:
    print("The users is senior")
    
    
