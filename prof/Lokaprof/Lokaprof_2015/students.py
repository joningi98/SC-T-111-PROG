class Students(object):
    def __init__(self, name='', grade=0):
        self.name = name
        self.grade = grade


def get_students():
    try:
        number_of_students = int(input("Enter number of students: "))
        student_list = []
        print("--- Reading students ---")
        for x in range(number_of_students):
            student_name = Students.name = input("Enter the name of the student: ")
            student_grade = Students.grade = float(input("Enter the grade of the Student: "))
            student = [student_name, student_grade]
            student_list.append(student)
            print("")
        return student_list
    except ValueError:
        print("Invalid input")
        quit()


def find_average(my_list):
    grades = []
    for x in my_list:
        grades.append(x[1])
    return grades


def main():
    student_list = get_students()
    grade_list = find_average(student_list)
    print("Average grade: {}".format(("%.2f" % (sum(grade_list) / len(grade_list)))))


main()