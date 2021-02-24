# Python OOP Tutorial 1: Classes and Instances
# class Employee:

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

# emp_1 = Employee('Joey', 'Tierney', 50000)
# emp_2 = Employee('Patton', 'Tierney', 60000)

# emp_1.fullname()
# print(Employee.fullname(emp_1))

# Python OOP Tutorial 2: Class Variables
# class Employee:

#     num_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# emp_1 = Employee('Joey', 'Tierney', 50000)
# emp_2 = Employee('Patton', 'Tierney', 60000)

# print(Employee.num_of_emps)

# Python OOP Tutorial 3: classmethods and staticmethods
# class Employee:

#     num_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)

#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True

# emp_1 = Employee('Joey', 'Tierney', 50000)
# emp_2 = Employee('Patton', 'Tierney', 60000)

# emp_str_1 = 'Rommel-Tee-70000'
# emp_str_2 = 'Chester-Paul-30000'
# emp_str_3 = 'Max-Peter-90000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# import datetime
# my_date = datetime.date(2021, 1, 14)

# print(Employee.is_workday(my_date))

# Python OOP Tutorial 4: Inheritance - Creating Subclasses
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

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
            print('-->', emp.fullname())

dev_1 = Developer('Joey', 'Tierney', 50000, 'Java')
dev_2 = Developer('Patton', 'Tierney', 60000, 'Python')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)