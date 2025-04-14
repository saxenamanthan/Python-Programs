print("Grading System")
marks = input("Enter your percentage - ")
marks = float(marks)
if marks > 100:
    print("Invalid Input!!!\nMarks cannot be more than 100")
elif 90 < marks <= 100:
    print("Your grade is A+")
elif 80 < marks <=90:
    print("Your grade is A")
elif 70 < marks <= 80:
    print("Your grade is B+")
elif 60 < marks <= 70:
    print("Your grade is B")
elif 50 < marks <= 60:
    print("Your grade is C+")
elif 40 < marks <= 50:
    print("Your grade is C")
else:
    print("You are Fail")
	