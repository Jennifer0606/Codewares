"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, S.

Constraints

0 < len(S) < 1000
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, S.

Sample Input
chris alan

Sample Output
Chris Alan
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    new_string = ""
    s = s.split(" ")
    for i in s:
        new_string += i.capitalize()+' '
    return new_string

    # other way
    # s1 = ''
    # for i in s.split(' '):
    #     s1 += i.capitalize()+' '
    # return s1

    ## best way
    # return ' '.join([name.capitalize() for name in s.split(' ')])


print(solve("chris alan"))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = solve(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()
