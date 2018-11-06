class Person(object):
    def __init__(self, name="", username="", ssn=0):
        self.name = name
        self.username = username
        self.ssn = ssn

    def get_name(self):
        return self.name

    def get_user_name(self):
        return self.username

    def get_ssn(self):
        return self.ssn


class Student(Person):
    def __init__(self, name="", username="", ssn=0, department=""):
        super().__init__(name, username, ssn)
        self.department = department

    def get_department(self):
        return self.department


class Professor(Person):
    def __init__(self, name="", username="", ssn=0, position=""):
        super().__init__(name, username, ssn)
        self.position = position

    def get_position(self):
        return self.position


class Course(Student, Professor):
    def __init__(self, name="", students=[], professor=Professor):
        super().__init__(name)
        self.students = students
        self.professor = professor

    def get_students(self):
        name_of_students = []
        for Student in self.students:
            name_of_students.append(Student.name)
        return name_of_students

    def get_professor(self):
        return self.professor.name


s1 = Student("Jón Jónsson", "jonj", 1, "IT")
s2 = Student("Gunna H.", "gunh", 2, "ET")
s3 = Student("Karl Magnússon.", "kalli", 3, "AT")

p1 = Professor("Tómas Bergsson", "tommi", 4, "Lektor")

c1 = Course("Stærðfræði", [s1, s2, s3], p1)

print(s2.get_name())
print(p1.get_position())
print(c1.get_name())
print(c1.get_students())
print(c1.get_professor())