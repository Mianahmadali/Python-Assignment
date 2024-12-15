#Can a ternary operator handle nested conditions? Provide an example to explain this.
#yes it is possible
marks = int(input("Enter your marks :"))
Grades = "A+" if marks >=90 else "A" if marks >=80 else "B" if marks >= 70  else "C"
print(Grades)