#Ask the user for a grade percentage and display the correspondig letter grade(A,B,C,D,F)
num=int(input("Enter your marks percentage"))
if num>=90:
    print("A+")
elif num>=80:
    print("A")
elif num>=70:
    print("B")
elif num>=60:
    print("C")
elif num>=33 and num<60:
    print("D")
else:
    print("F")
