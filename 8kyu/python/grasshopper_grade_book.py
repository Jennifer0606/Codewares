"""
https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
Grade book
Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""


# my solution
def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"


# best solution
# def get_grade(s1, s2, s3):
#     mean = sum([s1, s2, s3]) / 3
#     if mean >= 90: return 'A'
#     if mean >= 80: return 'B'
#     if mean >= 70: return 'C'
#     if mean >= 60: return 'D'
#     return 'F'


print('should return an A')
print(get_grade(95, 90, 93))
print(get_grade(100, 85, 96))
print(get_grade(92, 93, 94))
print(get_grade(100, 100, 100))

print("should return a B")
print(get_grade(70, 70, 100))
print(get_grade(82, 85, 87))
print(get_grade(84, 79, 85))

print("should return a C")
print(get_grade(70, 70, 70))
print(get_grade(75, 70, 79))
print(get_grade(60, 82, 76))

print("should return a D")
print(get_grade(65, 70, 59))
print(get_grade(66, 62, 68))
print(get_grade(58, 62, 70))

print("should return an F")
print(get_grade(44, 55, 52))
print(get_grade(48, 55, 52))
print(get_grade(58, 59, 60))
print(get_grade(0, 0, 0))
