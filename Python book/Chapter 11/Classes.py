class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(emp_1.first, emp_1.last)


emp_1 = Employee('John', 'Olaf', '600000')


print(emp_1.email)

print(emp_1.full_name())

print(Employee.full_name(emp_1))
