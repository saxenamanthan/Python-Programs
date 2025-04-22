student_marks = {
	"Akshat" : 85,
	"Bilal" : 72,
	"Chitransh" : 90
	}
#if you want only keys use this method    
for i in student_marks:
    print(i)

#if you want only values of dictionary use this method    
for i in student_marks.values():
    print(i)

#if you want both keys and values use this method    
for name,score in student_marks.items():
    print(f"The name of the student is {name} with score {score}")

#if you want both keys and values use this method   
for i in student_marks:    
    print(f"The name of the student is {i} with score {student_marks[i]}")
    