#Take three sides of a triangle as input and check if they form  valid triangle.
#we take three sides of triangle as (a,b.c)
a=int(input("Enter triangle side a value as int"))
b=float(input("Enter triangle side b value as float"))
c=int(input("Enter triangle side c value as int"))
if a+b>c and b+c>a and c+a>b:
    print("The triangle is valid")
else:
    print("The traiagle is unvalid")