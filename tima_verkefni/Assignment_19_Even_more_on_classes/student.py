
class Student(object):
    def __init__(self, student_id, grade):
        self.student = student_id
        self.grades = grade

    def get_grades(self):
        grade_list = []
        for x in self.grades:
            y = float(x)
            grade_list.append(y)
        print(grade_list)
        return grade_list

    def __gt__(self, other):
        return sum(self.get_grades()) > sum(other.get_grades())

    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.student, self.get_grades())


def main():
    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    john = Student(student_id, grades)

    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    alice = Student(student_id, grades)

    print("John's info")
    print(john)

    if john < alice:
        print("John has a lower average grade than Alice")
    else:
        print("Alice has a lower average grade than John")


main()