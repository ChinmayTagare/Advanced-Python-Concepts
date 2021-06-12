# -*- coding: utf-8 -*-
"""
Topic  : Decorators in Python
Author : Chinmay Tagare
 
"""

def decorator_function(func):
    print('in decorator function')
    print(func.__name__)
    def wrapper_function(*args, **kwargs):
        print('inside wraper function')
        return func(*args, **kwargs)
    return wrapper_function
    


@decorator_function
def display():
    print('in display function')
    var1 = 'variable in display function'
    print(var1)
    

@decorator_function
def display_info(name, age):
    print(name, age)
    

display()
print()
display_info('John', 25)


# Example of returning function from function
"""
def create_adder(x): 
    def adder(y): 
        return x+y 
  
    return adder 
  
add_15 = create_adder(15) 
  
print(add_15(10))

"""








