"""
https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python
Task
Given a Divisor and a Bound , Find the largest integer N , Such That ,

Conditions :
N is divisible by divisor

N is less than or equal to bound

N is greater than 0.

Notes
The parameters (divisor, bound) passed to the function are only positive values .
It's guaranteed that a divisor is Found .
Input >> Output Examples
maxMultiple (2,7) ==> return (6)
Explanation:
(6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .

maxMultiple (10,50)  ==> return (50)
Explanation:
(50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .*

maxMultiple (37,200) ==> return (185)
Explanation:
(185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 .
"""


# my solution
def max_multiple(divisor, bound):
    for i in range(bound, 0, -1):
        if i % divisor == 0 and i > 0:
            return i


# best solution
# def max_multiple(divisor, bound):
#     return bound - (bound % divisor)


# other solution
# def max_multiple(divisor, bound):
#     return bound // divisor * divisor


print(max_multiple(2, 7))  # return 6
print(max_multiple(3, 10))  # return 9
print(max_multiple(7, 17))  # return 14
print(max_multiple(10, 50))  # return 50
print(max_multiple(37, 200))  # return 185
print(max_multiple(7, 100))  # return 98
