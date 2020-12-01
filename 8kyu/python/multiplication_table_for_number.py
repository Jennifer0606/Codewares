"""
https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python
Your goal is to return multiplication table for number that is always an integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:

1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
P. S. You can use \n in string to jump to the next line.
"""


# my solution
def multi_table(number):
    result = []
    for i in range(1, 11):
        result.append(''.join("{} * {} = {}").format(i, number, i * number))
    return "\n".join(result)


# best solution
# def multi_table(number):
#     return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))


print(multi_table(5))  # return '1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50'
print(multi_table(1))  # return '1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10'
