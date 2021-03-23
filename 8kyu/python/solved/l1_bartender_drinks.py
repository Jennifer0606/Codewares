"""
https://www.codewars.com/kata/568dc014440f03b13900001d/train/python
Write a function getDrinkByProfession/get_drink_by_profession() that receives as input parameter a string,
    and produces outputs according to the following table:

Input	Output
"Jabroni"	"Patron Tequila"
"School Counselor"	"Anything with Alcohol"
"Programmer"	 "Hipster Craft Beer"
"Bike Gang Member"	"Moonshine"
"Politician"	"Your tax dollars"
"Rapper"	"Cristal"
*anything else*	"Beer"
Note: anything else is the default case:
    if the input to the function is not any of the values in the table, then the return value should be "Beer."

Make sure you cover the cases where certain words do not show up with correct capitalization.
For example, getDrinkByProfession("pOLitiCIaN") should still return "Your tax dollars".
"""
db = {
    "Jabroni": "Patron Tequila",
    "School Counselor": "Anything with Alcohol",
    "Programmer": "Hipster Craft Beer",
    "Bike Gang Member": "Moonshine",
    "Politician": "Your tax dollars",
    "Rapper": "Cristal"
}


# my solution
def get_drink_by_profession(param):
    for k, v in db.items():
        if k.lower() == param.lower():
            return v
    return "Beer"


print(get_drink_by_profession("jabrOni"))  # return "Patron Tequila"
print(get_drink_by_profession("scHOOl counselor"))  # return "Anything with Alcohol"
print(get_drink_by_profession("prOgramMer"))  # return "Hipster Craft Beer"
print(get_drink_by_profession("bike ganG member"))  # return "Moonshine"
print(get_drink_by_profession("poLiTiCian"))  # return "Your tax dollars"
print(get_drink_by_profession("rapper"))  # return "Cristal"
print(get_drink_by_profession("pundit"))  # return "Beer"
print(get_drink_by_profession("Pug"))  # return "Beer"
