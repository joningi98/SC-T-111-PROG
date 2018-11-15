class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.full_name())





# dev_1 = Developer('Corey', 'Schafer', 50000, "Python")
# dev_2 = Developer('Test', 'Employee', 60000, 'Java')


# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# m gr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

#################################
emp_1 = Employee('Jon', 'Olafsson', 50000)
emp_2 = Employee('Bjarki', 'Magnússon', 60000)

print(emp_1 + emp_2)
print(len(emp_1))

# emp_srt_1 = 'John-Doe-70000'
# emp_srt_2 = 'Steve-Smith-30000'
# emp_srt_3 = 'Jane-Doe-90000'

# new_emp_1 = Employee.from_string(emp_srt_1)
# print(new_emp_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)
