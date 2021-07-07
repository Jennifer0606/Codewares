"""
https://www.codewars.com/kata/56170e844da7c6f647000063/train/python
Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples:

people_with_age_drink(13) == "drink toddy"
people_with_age_drink(17) == "drink coke"
people_with_age_drink(18) == "drink beer"
people_with_age_drink(20) == "drink beer"
people_with_age_drink(30) == "drink whisky"
"""


# my solution
def people_with_age_drink(age):
    if age >= 21:
        return "drink whisky"
    elif 14 <= age < 18:
        return "drink coke"
    elif 18 <= age < 21:
        return "drink beer"
    else:
        return "drink toddy"


# # best solution
# def people_with_age_drink(age):
#     if age > 20: return 'drink whisky'
#     if age > 17: return 'drink beer'
#     if age > 13: return 'drink coke'
#     return 'drink toddy'


# # other solution
# def people_with_age_drink(age):
#     if age <= 13:
#         beverage = 'toddy'
#     elif 13 < age <= 17:
#         beverage = 'coke'
#     elif 17 < age <= 20:
#         beverage = 'beer'
#     elif age > 20:
#         beverage = 'whisky'
#     return 'drink ' + beverage


print("should return 'drink toddy' when age is less than 14")
print(people_with_age_drink(13))  # return drink toddy', "Wrong result for 13"
print(people_with_age_drink(0))  # return drink toddy', "Wrong result for 0"

print("should return 'drink coke' when age is between 14(inclusive) and 18(exclusive)")
print(people_with_age_drink(17))  # return drink coke'
print(people_with_age_drink(15))  # return drink coke'
print(people_with_age_drink(14))  # return drink coke'

print("should return 'drink beer' when age is between 18(inclusive) and 21(exclusive)")
print(people_with_age_drink(20))  # return drink beer'
print(people_with_age_drink(18))  # return drink beer'

print("should return 'drink whisky' when age is greater than or equal to 21")
print(people_with_age_drink(22))  # return drink whisky'
print(people_with_age_drink(21))  # return drink whisky'
