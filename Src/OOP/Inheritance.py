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

# SUBCLASS
# in order to let super class handle first,last,pay
    # employee class already has those attributes,
    # instead of re-writing the init mehtod lines,
    # we can use super() to say - use super class for these variables
    # this is same as - but preferred as super()
    # Employee.__init__(self, first, last, pay)
    # dev class need prog_lang as additional attribute

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang



emp_1 = Employee('Ken', 'Adams', 40000)
emp_2 = Employee('Tag', 'James', 60000)

dev_1 = Developer('Corey', 'Schafer', 50000, 'Java')
dev_2 = Developer('Chinmay', 'Tagare', 80000, 'Python')

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print()
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.prog_lang)




