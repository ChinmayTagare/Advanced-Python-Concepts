# -*- coding: utf-8 -*-
"""
Topic  : Decorators in Python
Author : Chinmay Tagare
"""

def decor_2(func):
    def inner_2(*args, **kwargs):
        y = func(*args, **kwargs)
        return y*y
    return inner_2

def decor_1(func):
    def inner_1(*args, **kwargs):
        x = func(*args, **kwargs)
        return x*2
    return inner_1

@decor_1
@decor_2
def input_num(num):
    return num

# decor1(decor_2(input_num(10)))

print(input_num(10))