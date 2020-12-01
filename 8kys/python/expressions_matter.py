"""
https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python
Task
Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained
Consider an Example :
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is 9.
"""


# my solution
def expression_matter(a, b, c):
    first = a * (b + c)
    second = a * b * c
    third = (a + b) * c
    fourth = a + b + c
    return max(first, second, third, fourth)


# best solution
# def expression_matter(a, b, c):
#     return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))


print("Small values")
print(expression_matter(2, 1, 2))  # return 6
print(expression_matter(2, 1, 1))  # return 4
print(expression_matter(1, 1, 1))  # return 3
print(expression_matter(1, 2, 3))  # return 9
print(expression_matter(1, 3, 1))  # return 5
print(expression_matter(2, 2, 2))  # return 8

print("Medium values")
print(expression_matter(5, 1, 3))  # return 20
print(expression_matter(3, 5, 7))  # return 105
print(expression_matter(5, 6, 1))  # return 35
print(expression_matter(1, 6, 1))  # return 8
print(expression_matter(2, 6, 1))  # return 14
print(expression_matter(6, 7, 1))  # return 48

print("Mixed values")
print(expression_matter(2, 10, 3))  # return 60
print(expression_matter(1, 8, 3))  # return 27
print(expression_matter(9, 7, 2))  # return 126
print(expression_matter(1, 1, 10))  # return 20
print(expression_matter(9, 1, 1))  # return 18
print(expression_matter(10, 5, 6))  # return 300
print(expression_matter(1, 10, 1))  # return 12
