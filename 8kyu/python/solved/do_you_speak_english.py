"""
https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058/train/python
Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

Upper or lower case letter does not matter -- "eNglisH" is also correct.

Return value as boolean values, true for the string to contains "English", false for it does not.
"""


# my solution
def sp_eng(sentence):
    return True if "english" in sentence.lower() else False


# best solution
def sp_eng(sentence):
    return 'english' in sentence.lower()


print(sp_eng("english"))  # True
print(sp_eng("egnlish"))  # False
print(sp_eng("1234egn lis;h"))  # False
print(sp_eng("1234english ;k"))  # True
print(sp_eng("English"))  # True
print(sp_eng("eNgliSh"))  # True
print(sp_eng("1234#$%%eNglish ;k9"))  # True
print(sp_eng("EGNlihs"))  # False
print(sp_eng("1234englihs**"))  # False
print(sp_eng(""))  # False
