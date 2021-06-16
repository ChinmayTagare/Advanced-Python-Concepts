"""
Python Object Oriented Programming
Author : Chinmay Tagare
"""

# class is blueprint to create an instances
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Chinmay', 'Tagare', 50000)
emp2 = Employee('Test', 'User', 60000)

# =============================================================================
# emp1.first = 'Chinmay'
# emp1.last = 'Tagare'
# emp1.email = 'Chinmay.Tagare@company.com'
# emp1.pay = 50000
# 
# emp2.first = 'Test'
# emp2.last = 'User'
# emp2.email = 'Test.User@company.com'
# emp2.pay = 60000
# 
# =============================================================================
print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(Employee.fullname(emp2))