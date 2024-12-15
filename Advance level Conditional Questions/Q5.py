"""Create a Python program to classify a student's grade based on their score:
Score >= 90: "A"
80 <= Score < 90: "B"
70 <= Score < 80: "C"
Otherwise: "Fail"""
score = int(input("Enter Your Score :"))
if score >= 90:
    print("A")
elif score >= 80 and score <90 :
    print("B")
elif score >=70 and score < 80 :
    print("C") 
else:
    print("Fail")