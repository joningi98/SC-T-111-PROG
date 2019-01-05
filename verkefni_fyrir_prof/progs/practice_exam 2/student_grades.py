

def get_grades():
    grades = []
    count = 1
    for x in range(3):
        grade = float(input("Input grade number {}: ".format(count)))
        count += 1
        grades.append(grade)
    return grades


def get_highest_grade(students):
    highest_grade = 0.0
    student = ''
    for name, grades in students.items():
        average_grade = (sum(grades) / len(grades))
        if average_grade > highest_grade:
            highest_grade = average_grade
            student = name
    return highest_grade, student


def main():
    students_dict = {}
    for x in range(4):
        name = input("Input student name: ")
        grades = get_grades()
        students_dict[name] = grades
    print("Student list")
    for name, grades in sorted(students_dict.items()):
        print("{}: {}".format(name, grades))
    print()
    highest_grade, name = get_highest_grade(students_dict)
    print("Student with highest average grade:")
    print("{} has an average grade of {:.2f}".format(name, highest_grade))


main()