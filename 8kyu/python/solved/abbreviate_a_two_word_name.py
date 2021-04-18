"""
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
"""


# my solution
def abbrev_name(name):
    name = name.split(" ")
    name = name[0][0], name[1][0]
    return ('.'.join(name)).upper()


# best solution
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


# other solution
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]


print(abbrev_name("Sam Harris"))  # "S.H"
print(abbrev_name("Patrick Feenan"))  # "P.F"
print(abbrev_name("Evan Cole"))  # "E.C"
print(abbrev_name("P Favuzzi"))  # "P.F"
print(abbrev_name("David Mendieta"))  # "D.M"
