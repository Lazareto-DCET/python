class Student:
    def __init__(self, name):
        self.name = name
        self.homeworks = []
        self.seatworks = []
        self.quizzes = []
        self.midterm_exam = 0.0
        self.mg = 0.0
        self.pg = 0.0

    def compute_grade(self):
        hw_avg = sum(self.homeworks) / len(self.homeworks) if self.homeworks else 0
        sw_avg = sum(self.seatworks) / len(self.seatworks) if self.seatworks else 0
        qz_avg = sum(self.quizzes) / len(self.quizzes) if self.quizzes else 0

        self.mg = (
            hw_avg * 0.2 +
            sw_avg * 0.2 +
            qz_avg * 0.2 +
            self.midterm_exam * 0.4
        )

    def compute_point_grade(self):
        g = self.mg
        if g >= 96: self.pg = 1.00
        elif g >= 94: self.pg = 1.25
        elif g >= 91: self.pg = 1.50
        elif g >= 88: self.pg = 1.75
        elif g >= 85: self.pg = 2.00
        elif g >= 83: self.pg = 2.25
        elif g >= 80: self.pg = 2.50
        elif g >= 78: self.pg = 2.75
        elif g >= 75: self.pg = 3.00
        else: self.pg = 5.0


def get_scores(label, count):
    scores = []
    for i in range(1, count + 1):
        while True:
            try:
                score = float(input(f"Enter {label} {i}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input.")
    return scores


def main():
    print("=== Midterm Grade ===")

    n_students = int(input("Enter no. of students: "))
    n_homeworks = int(input("Enter no. of homeworks: "))
    n_seatworks = int(input("Enter no. of Seatworks: "))
    n_quizzes = int(input("Enter no. of Quiz: "))

    students = []

    for _ in range(n_students):
        print()
        name = input("Enter Student Name: ")
        s = Student(name)
        s.homeworks = get_scores("homework", n_homeworks)
        s.seatworks = get_scores("seatwork", n_seatworks)
        s.quizzes = get_scores("quiz", n_quizzes)
        s.midterm_exam = float(input("Enter Midterm Exam: "))
        s.compute_grade()
        s.compute_point_grade()
        students.append(s)

    print("\nSummary:")
    print(f"{'Name':<10} {'MG':>5} {'PG':>5}")
    for s in students:
        print(f"{s.name:<10} {s.mg:>5.0f} {s.pg:>5.2f}")


if __name__ == "__main__":
    main()
