"""
https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python
Definition
Jumping number is the number that All adjacent digits in it differ by 1.

Task
Given a number, Find if it is Jumping or not .

Notes
Number passed is always Positive .

Return the result as String .

The difference between ‘9’ and ‘0’ is not considered as 1 .

All single digit numbers are considered as Jumping numbers.

Input >> Output Examples
jumpingNumber(9) ==> return "Jumping!!"
Explanation:
It's single-digit number
jumpingNumber(79) ==> return "Not!!"
Explanation:
Adjacent digits don't differ by 1
jumpingNumber(23) ==> return "Jumping!!"
Explanation:
Adjacent digits differ by 1
jumpingNumber(556847) ==> return "Not!!"
Explanation:
Adjacent digits don't differ by 1
jumpingNumber(4343456) ==> return "Jumping!!"
Explanation:
Adjacent digits differ by 1
jumpingNumber(89098) ==> return "Not!!"
Explanation:
Adjacent digits don't differ by 1
jumpingNumber(32) ==> return "Jumping!!"
Explanation:
Adjacent digits differ by 1
"""


def jumping_number(number):
    while len(str(number)) == 1:
        return "Jumping!!"

    number = [int(x) for x in str(number)]
    for i in range(len(number)-1):
        if number[i+1] != number[i] + 1 and number[i+1] != number[i] - 1:
            return "Not!!"
    return "Jumping!!"


# best solution
# def jumping_number(number):
#     arr = list(map(int, str(number)))
#     return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]


print("Single Digit Number")
print(jumping_number(1))  # return "Jumping!!"
print(jumping_number(7))  # return "Jumping!!"
print(jumping_number(9))  # return "Jumping!!"

print("Two Digit Number")
print(jumping_number(23))  # return "Jumping!!"
print(jumping_number(32))  # return "Jumping!!"
print(jumping_number(79))  # return "Not!!"
print(jumping_number(98))  # return "Jumping!!"

print("Larger Numbers")
print(jumping_number(8987))  # return "Jumping!!"
print(jumping_number(4343456))  # return "Jumping!!"
print(jumping_number(98789876))  # return "Jumping!!"
