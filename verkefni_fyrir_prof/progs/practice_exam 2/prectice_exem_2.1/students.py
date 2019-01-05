def create_students():
    students = {}
    for x in range(4):
        name = input("Student name: ")
        grades = []
        count = 1
        for y in range(3):
            grade = float(input("Input grade number {}: ".format(count)))
            count += 1
            grades.append(grade)
        students[name] = grades
    return students


def print_students(students):
    print("Student list")
    for name, grades in students.items():
        print("{}: {}".format(name, grades))


def highest_grade(student_list):
    highest_average_grade = 0.0
    name_highest = ''
    for name, grade in student_list.items():
        average_grade = sum(grade) / len(grade)
        if average_grade > highest_average_grade:
            highest_average_grade = average_grade
            name_highest = name
    return name_highest, highest_average_grade


def main():
    student_list = create_students()
    print_students(student_list)
    highest_grade(student_list)
    name, average_grade = highest_grade(student_list)
    print()
    print("Student with highest average grade:\n{} has an average grade of {:.2f}".format(name, average_grade))


main()
