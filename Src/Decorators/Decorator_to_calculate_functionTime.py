# -*- coding: utf-8 -*-
"""
Topic  : Decorators in Python
Author : Chinmay Tagare
"""

import time
import math

# Define decorator function
def calculate_time(main_func):
    
    def inner_func(*args, **kwargs):
        
        begin = time.time()
        
        main_func(*args, **kwargs)
        
        end = time.time()
        print('Total time taken = {}'.format(end-begin))
        
    return inner_func


@calculate_time
def sqr_func(limit):
    sqrs = [x*x for x in range(limit)]
    return sqrs


@calculate_time
def factorial_func(limit):
    fact_result = math.factorial(limit)
    print(fact_result)
    return fact_result

sqr_func(1000000)
print('---------')
factorial_func(25)