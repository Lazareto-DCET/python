student=list()
seatwork=list()
homework=list()
quiz=list()

studentname=input("Enter your name: ")
print("\n=================================")
num_sw = int(input("Input your amount of Seatworks you did in midterm: "))
for i in range(num_sw):
    swgrade=float(input("Enter your grade in seatwork " +str(i+1) + ": "))
    seatwork.append(swgrade)

print("\n=================================")
num_hw = int(input("Input your amount of Homeworks you did in midterm: "))
for i in range(num_hw):
    hwgrade=float(input("Enter your grade in homework " +str(i+1) +": "))
    homework.append(hwgrade)

print("\n=================================")
num_qz = int(input("Input your amount of Quizzes you did in midterm: "))
for i in range(num_qz):
    qzgrade=float(input("Enter your grade in quiz " +str(i+1) + ": "))
    quiz.append(qzgrade)

print("\n=================================")
num_mid = int(input("Enter your Midterm Exam Grade: "))

seatwork_avg=sum(seatwork)/len(seatwork)
homework_avg=sum(homework)/len(homework)
quiz_avg=sum(quiz)/len(quiz)
exam_avg=num_mid*0.30
csm_avg=(seatwork_avg*0.20)+(homework_avg*0.20)+(quiz_avg*0.60)
final_avg=(csm_avg*0.70)+(num_mid*0.30)

print("\nYour student name:", studentname)
print("=================================")
print("CSM Average:", round(csm_avg,2),"%")
print("\nCSM Components:")
print("Seatwork Average:", round(seatwork_avg,2),"%")
print("Homework Average:", round(homework_avg,2),"%")
print("Quiz Average:", round(quiz_avg,2),"%")
print("=================================")
print("Exam Average:", round(exam_avg,2),"%")
print("=================================")
print("Midterm Average:", round(final_avg,2),"%")
