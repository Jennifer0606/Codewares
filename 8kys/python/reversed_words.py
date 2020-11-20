"""
Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
"""


# My answer
def reverseWords(s):
    a = s.split(" ")
    a.reverse()
    return " ".join(a)


# Best Solution
# def reverseWords(s):
#     return " ".join(s.split(" ")[::-1])


print(reverseWords("hello world!"))  # should return  "world! hello"
