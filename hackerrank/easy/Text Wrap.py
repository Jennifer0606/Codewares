"""
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, string.
The second line contains the width, maxwidth.

Constraints

0 < len(string) < 100
0 < maxwidth < len(string)

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap


def wrap(string, max_width):
    # new_list = textwrap.wrap(string, max_width)
    # new_string = ""
    # for i in new_list:
    #     new_string += i + '\n'
    # return new_string

    # best way
    a = textwrap.wrap(string, max_width)
    a = "\n".join(a)
    return a


print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)
