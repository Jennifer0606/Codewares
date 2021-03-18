"""
https://www.codewars.com/kata/56f173a35b91399a05000cb7/train/python
Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value.
Output should be the length of the longest word, as a number.
"""


# my solution
def find_longest(string):
    spl = string.split(" ")
    # print(spl)
    longest = 0
    for i in spl:
        count = spl(i)
        if count > longest:
            longest = count
    return longest
    # i = 0
    # while i > spl.length:
    #     if spl(i).length > longest: longest = spl[i].length
    # return longest


print(find_longest("The quick white fox jumped around the massive dog"))  # return 7
print(find_longest("Take me to tinseltown with you"))  # return 10
print(find_longest("Sausage chops"))  # return 7
print(find_longest("Wind your body and wiggle your belly"))  # return 6
print(find_longest("Lets all go on holiday"))  # return 7
