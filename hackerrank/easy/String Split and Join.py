"""
In Python, a string can be split on a delimiter.

Example:

a = "this is a string"
a = a.split(" ") # a is converted to a list of strings.
print a
['this', 'is', 'a', 'string']
Joining a string is simple:

a = "-".join(a)
print a
this-is-a-string
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
Input Format
The one line contains a string consisting of space separated words.
"""


def split_and_join(line):
    # split() 方法將字串根據指定的分隔符分割成子字串，並返回一個由這些子字串組成的列表。
    # ['this', 'is', 'a', 'string']
    # join() 方法將一個列表中的元素連結起來，並返回一個字串。
    return "-".join(line.split(" "))


# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

print(split_and_join("this is a string"))
