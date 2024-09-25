class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def display(self):
        average_grade = self.calculate_average()
        print(f"Student Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average_grade:.2f}")


student = Student("John Doe")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)
student.display()