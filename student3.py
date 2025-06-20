from tabulate import tabulate

print("\n==============================")
print("============Subject===========")
print("==============================")

students = []
num_students = int(input("Number of Students: "))
subject = input("What is the subject you would like to calculate? ")

num_assignments = int(input("\nHow many assignments? "))
num_seatworks = int(input("How many seat works? "))
num_quizzes = int(input("How many quizzes? "))


for _ in range(num_students):
    print("\n==============================")
    name = input("Enter Student Name: ")

    assignments = []
    for i in range(num_assignments):
        score = float(input(f"Enter homework {i+1}: "))
        assignments.append(score)

    seatworks = []
    for i in range(num_seatworks):
        score = float(input(f"Enter seatwork {i+1}: "))
        seatworks.append(score)

    quizzes = []
    for i in range(num_quizzes):
        score = float(input(f"Enter quiz {i+1}: "))
        quizzes.append(score)

    exam = float(input("Enter Midterm Exam score: "))

   
    assignment_avg = sum(assignments) / len(assignments)
    seatwork_avg = sum(seatworks) / len(seatworks)
    quiz_avg = sum(quizzes) / len(quizzes)

    avg_total = (assignment_avg * 0.20) + (seatwork_avg * 0.20) + (quiz_avg * 0.60)
    midterm_grade = (avg_total * 0.30) + (exam * 0.70)

    
    if midterm_grade == 75:
        point_grade = 3.00
        remarks = "Passing"
    elif 76 <= midterm_grade <= 78:
        point_grade = 2.75
        remarks = "Passing"
    elif 79 <= midterm_grade <= 81:
        point_grade = 2.50
        remarks = "Passing"
    elif 82 <= midterm_grade <= 84:
        point_grade = 2.25
        remarks = "Good"
    elif 85 <= midterm_grade <= 87:
        point_grade = 2.00
        remarks = "Good"
    elif 88 <= midterm_grade <= 90:
        point_grade = 1.75
        remarks = "Excellent"
    elif 91 <= midterm_grade <= 93:
        point_grade = 1.50
        remarks = "Excellent"
    elif 94 <= midterm_grade <= 96:
        point_grade = 1.25
        remarks = "Excellent"
    elif 97 <= midterm_grade <= 100:
        point_grade = 1.00
        remarks = "Excellent"
    else:
        point_grade = 5.00
        remarks = "FAILURE"

   
    students.append([name, round(midterm_grade, 2), point_grade, remarks])


print("\n======== Summary ========")
print(f"==========={subject}==========")
print(tabulate(students, headers=["Name", "Midterm Grade", "Point Grade", "Remarks"], tablefmt="fancy_grid"))
