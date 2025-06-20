class Student:
    def __init__(self, name, seatwork, quiz, homework, exam):
        self.name = name
        self.seatwork = seatwork
        self.quiz = quiz
        self.homework = homework
        self.exam = exam
        self.grade = 0.0
        self.point = 0.0

    def compute_grade(self, weights):
        self.grade = (
            self.seatwork * weights['seatwork'] +
            self.quiz * weights['quiz'] +
            self.homework * weights['homework'] +
            self.exam * weights['exam']
        )

    def compute_point(self):
        g = self.grade
        if g >= 96: self.point = 1.00
        elif g >= 94: self.point = 1.25
        elif g >= 91: self.point = 1.50
        elif g >= 88: self.point = 1.75
        elif g >= 85: self.point = 2.00
        elif g >= 83: self.point = 2.25
        elif g >= 80: self.point = 2.50
        elif g >= 78: self.point = 2.75
        elif g >= 75: self.point = 3.00
        else: self.point = 5.00

def get_amount(prompt):
    while True:
        try:
            val = int(input(prompt))
            if 0 <= val:
                return val
            print("Please enter the specific amount.")
        except ValueError:
            print("Invalid input. Try again.")
            
def get_score(prompt):
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= 100:
                return val
            print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Try again.")


def main():
    print("=== Midterm Grade ===")

    weights = {
        "seatwork": 0.2,
        "quiz": 0.3,
        "homework": 0.2,
        "exam": 0.3
    }

    students = []

    while True:
        num_st = get_amount("Enter no. of students: ")
        num_hw = get_amount("Enter no. of homeworks: ")
        num_sw = get_amount("Enter no. of seatworks: ")
        num_qz = get_amount("Enter no. of quizzes: ")
        for i in range(num_st):
            name = input("\nEnter student name: ")
            for i in range(num_hw):
                homework = get_score("Enter homework " +str(i+1) + " score: ")
            for i in range(num_sw):
                seatwork = get_score("Enter seatwork " +str(i+1) + " score: ")
            for i in range(num_qz):
                quiz = get_score("Enter quiz " +str(i+1) + " score: ")
        
            exam = get_score("Enter midterm exam score: ")

            student = Student(name, seatwork, quiz, homework, exam)
            student.compute_grade(weights)
            student.compute_point()
            students.append(student)


    print("\n=== Grade Summary ===")
    print("{:<20} {:>8} {:>10}".format("Name", "Grade", "Point"))
    print("-" * 40)
    for s in students:
        print(f"{s.name:<20} {s.grade:>8.2f} {s.point:>10.2f}")


if __name__ == "__main__":
    main()
