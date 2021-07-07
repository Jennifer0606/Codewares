"""
https://www.codewars.com/kata/5a2b703dc5e2845c0900005a/train/python
Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.

A few cases:


(-12, 2, -6)  ->  true
(-12, 2, -5)  ->  false

(45, 1, 6)    ->  false
(45, 5, 15)   ->  true

(4, 1, 4)     ->  true
(15, -5, 3)   ->  true
"""


# my solution
def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0


# best solution
# def is_divide_by(number, a, b):
#     return number % a == 0 and number % b == 0

print(is_divide_by(-12, 2, -6))  # return True
print(is_divide_by(-12, 2, -5))  # return  False
print(is_divide_by(45, 1, 6))  # return  False
print(is_divide_by(45, 5, 15))  # return True
print(is_divide_by(4, 1, 4))  # return True
print(is_divide_by(15, -5, 3))  # return True)
