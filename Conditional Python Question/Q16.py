#Take the length of three sides and classify the riangle is (equilateral,isosceles or scalene).
a=int(input("Enter length of a triangle side a :"))
b=int(input("Enter length of a triangle side b :"))
c=int(input("Enter length of a triangle side c :"))
#a,b,c are three sides of a triangle
if a==b and b==c and c==a:
    print("The triangle is isoscales")
elif a==b==c:
    print("The triangle is equilateral")
else:
    print("The triangle is scalene")