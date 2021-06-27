"""
Python Object Oriented Programming
Author : Chinmay Tagare
"""
# code example for regular method, class methods and static methods


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
        
        # regular method automatically takes instance as first argument
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
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_string):
        first,last,pay = emp_string.split('-')
        return cls(first,last,pay)


emp1 = Employee('Chinmay', 'Tagare', 50000)
emp2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)
# the above statement is same as saying Employee.raise_amt = 1.05
# but we have set class method - sets the class variable value in cls.raise_amt

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

emp_str1 = 'Rahul-sathye-20000'
emp_str2 = 'Sarang-Kulkarni-50000'
emp_str3 = 'Arjun-jp-80000'

# normal way - without class methods
first,last,pay = emp_str1.split('-')
new_emp1 = Employee(first, last, pay)

# with class method
new_emp2 = Employee.from_string(emp_str2)


print(new_emp1.email)
print(new_emp2.email)







