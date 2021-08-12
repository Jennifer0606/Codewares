"""
https://www.codewars.com/kata/55eca815d0d20962e1000106/train/python
Implement a function named generateRange(min, max, step), which takes three arguments and generates a range of integers from min to max, with the step. The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)
Task

Implement a function named

generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
generate_range(1, 10, 3) # should return list of [1,4,7,10]

generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]

Note

    min < max
    step > 0
    the range does not HAVE to include max (depending on the step)

"""


# my solution
def generate_range(min, max, step):
    res = []
    new_num = min
    while new_num <= max:
        res.append(new_num)
        new_num = new_num + step
    return res


# best solution
def generate_range(min, max, step):
    return list(range(min, max + 1, step))


print(generate_range(1, 10, 1))  # return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(generate_range(-10, 1, 1))  # return [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
print(generate_range(1, 15, 20))  # return [1]
print(generate_range(1, 7, 2))  # return  [1, 3, 5, 7]
print(generate_range(0, 20, 3))  # return [0, 3, 6, 9, 12, 15, 18]
