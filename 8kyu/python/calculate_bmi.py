"""
https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""


# my solution
def bmi(weight, height):
    bmi_result = weight / (height ** 2)
    if bmi_result <= 18.5:
        return "Underweight"
    elif bmi_result <= 25.0:
        return "Normal"
    elif bmi_result <= 30.0:
        return "Overweight"
    else:
        return "Obese"


# clever solution
# def bmi(weight, height):
#     b = weight / height ** 2
#     return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]


print(bmi(50, 1.80))  # return "Underweight"
print(bmi(80, 1.80))  # return "Normal"
print(bmi(90, 1.80))  # return "Overweight"
print(bmi(110, 1.80))  # return "Obese"
print(bmi(50, 1.50))  # return "Normal"
