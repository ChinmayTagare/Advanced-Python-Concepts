"""
Python Object Oriented Programming
Author : Chinmay Tagare
"""
# this is to define the difference between instance variable and class variable


# class is blueprint to create an instances
class Employee:
    
    # class variable - using self.class_var will make is as instance variable
    raise_amt = 1.04
    
    # class variable to get the count of emps
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        # not used self here bcoz
        # dont want to change the count of emps 
        # based on instance so its not instance variable, its class variable
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
# =============================================================================
#     # hard coded raise in class, but we want to be as variable
#     def apply_raise(self):
#         self.pay = int(self.pay * 1.04)
# =============================================================================
    # self.raise_amt in below command will allow us to change the 
    # class variable value for perticular instance
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp1 = Employee('Chinmay', 'Tagare', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# checking in namespace
# class obj will not have class variable as attribute
print(emp1.__dict__)
# but class dict will have class variable
print(Employee.__dict__)

# to change the class variable - 
# it will change for all the instances
Employee.raise_amt = 1.05

# =============================================================================
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)
# =============================================================================
# to change the class variable for an instance
emp1.raise_amt = 1.06
# it will change for only this instance
# =============================================================================
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)
# =============================================================================
# now after assignment, if we check in namespace,
# class variable will be present for that instance (emp1)
print(emp1.__dict__)


print('----------class variable 2-------------------')
print(Employee.num_of_emps)


