"""
https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""


# My answer
def square_sum(numbers):
    answer = 0
    for i in range(len(numbers)):
        answer = answer + (numbers[i] ** 2)
    return answer


# solution1
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)


print(square_sum([1, 2]))  # should return , 5
print(square_sum([0, 3, 4, 5]))  # should return 50
