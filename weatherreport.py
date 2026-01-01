
students_details = []
for _ in range(int(input("Enter the number of students: "))):
    name = input("Enter the student's name: ")
    score = float(input("Enter the student's grade: "))
    students_details.append([name,score])


second_last = sorted(students_details,key=lambda x:(-x[1],x[0]))[2]
print(second_last)




    