#!/usr/bin/python3
# -*- coding: utf-8 -*-

def avg(nums):
    return sum(nums) / len(nums)

def drop_first_last(grades):
    """drop the first and last grade, return the average"""
    first, *middle, last = grades
    return avg(middle)

# should print 2.5
print(float(drop_first_last([1, 2, 3, 4])))

