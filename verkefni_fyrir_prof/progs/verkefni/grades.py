

def open_file(file_name):
    students = []
    with open(file_name, "r") as file:
        for name in file.readlines():
            students.append(name.strip())
    return students


def find_grade(students):
    students_dict = {}
    for name in students:
        grade = 0
        for letter in name:
            if letter != " ":
                grade += ord(letter)
        students_dict[name] = grade

    return students_dict


def find_highest_grade(my_dict):
    highest_grade = 0
    name_with_grade = ""
    for name, grade in my_dict.items():
        if grade > highest_grade:
            highest_grade = grade
            name_with_grade = name

    print(highest_grade)
    print(name_with_grade)


def main():
    file_name = "names.txt"
    students = open_file(file_name)
    student_dict = find_grade(students)
    find_highest_grade(student_dict)


main()


