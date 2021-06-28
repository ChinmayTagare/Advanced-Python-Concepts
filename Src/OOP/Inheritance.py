"""
Python Object Oriented Programming
Author : Chinmay Tagare
"""

class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

# SUBCLASS 1
# in order to let super class handle first,last,pay employee class already has those attributes,
    # instead of re-writing the init mehtod lines, we can use super() to say - use super class for these variables
    # this is same as - but preferred as super() Employee.__init__(self, first, last, pay)
    # dev class need prog_lang as additional attribute

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

# SUBCLASS 2
# good idea is to pass none as argument and then create empty list in if condition
# instead of passing empty list as argument
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None):
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
            print('--> ', emp.fullname())

emp_1 = Employee('Ken', 'Adams', 40000)
emp_2 = Employee('Tag', 'James', 60000)

dev_1 = Developer('Corey', 'Schafer', 50000, 'Java')
dev_2 = Developer('Chinmay', 'Tagare', 80000, 'Python')

print('----------------1---------------')
# using class
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print('-----------------2--------------')
# using subclass 1
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.prog_lang)

print('----------------3---------------')
# using subclass 2
mgr_1 = Manager('Jack', 'lee', 90000, [dev_2])
print(mgr_1.email)
mgr_1.print_emps()

print('-----------------4--------------')
mgr_1.add_emp(dev_1)
mgr_1.print_emps()

print('-----------------5--------------')
# built in functions for class in python
# to check if the object is an instance of a class
print(isinstance(mgr_1, Manager))





