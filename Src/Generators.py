# -*- coding: utf-8 -*-
"""
Topic  : Generators in Python
Author : Chinmay Tagare

"""

import time

# Traditional way 
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = [i for i in range(10000000)]

time1 = time.time()
res = square_numbers(my_nums)
print(time.time() - time1)
# print(res)


# use of generators
# Generators don't hold entire result in memory
# returns the generator object
# It yields one result at a time when it is asked to
def square_numbers_generator(nums):
    for i in nums:
        yield(i*i)

my_nums_new = [i for i in range(10000000)]
time1 = time.time()
res_g = square_numbers_generator(my_nums_new)
print(time.time() - time1)
# print(res_g)


# List comperhension

nums_lst = [x*x for x in range(10)]
print(nums_lst)

nums_generator = (x*x for x in range(10))
print(nums_generator)


# INSIGHTS

# GENERATORS ARE BETTER WITH PERFORMANCE FOR LARGE DATA




