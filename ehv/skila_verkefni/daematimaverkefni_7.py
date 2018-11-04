class Person(object):
    def __init__(self, name='', username='', ssn=0):
        self.name = name
        self.User_name = username
        self.SSN = ssn

    def getName(self):
        return self.name

    def get_user_name(self):
        return self.User_name

    def get_SSN(self):
        return self.SSN


class Student(Person):
    def __init__(self, department=''):
        super().__init__()
        self.department = department

    def get_department(self):
        return self.department


class Professor(Person):
    def __init__(self, position=''):
        super().__init__()
        self.position = position

    def get_position(self):
        return self.position


class Course(Professor, Student):
    def __init__(self, name='', students=1, professor=Professor):
        super().__init__()
        self.course_name = name
        self.students = students
        self.Professor = professor

    def get_name(self):
        return self.course_name

    def get_students(self):
        return self.students

    def get_professor(self):
        return self.Professor


