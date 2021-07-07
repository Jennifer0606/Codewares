"""
https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
"""


# my solution
def check(seq, elem):
    return elem in seq


# best solution
def check(seq, elem):
    return elem in seq


print(check([66, 101], 66))  # true
print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))  # false
print(check([101, 45, 75, 105, 99, 107], 107))  # true
print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))  # true
print(check(['t', 'e', 's', 't'], 'e'))  # true
print(check(["what", "a", "great", "kata"], "kat"))  # false
print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups"))  # true
print(check(["come", "on", 110, "2500", 10, '!', 7, 15], "Come"))  # false
print(check(["when's", "the", "next", "Katathon?", 9, 7], "Katathon?"))  # true
print(check([8, 7, 5, "bored", "of", "writing", "tests", 115], 45))  # false
print(check(["anyone", "want", "to", "hire", "me?"], "me?"))  # true
