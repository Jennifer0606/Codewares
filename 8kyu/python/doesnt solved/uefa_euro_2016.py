"""
https://www.codewars.com/kata/57613fb1033d766171000d60/train/python
Finish the uefaEuro2016() function so it return string just like in the examples below:
uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."
"""


# best solution
# def uefa_euro_2016(teams, scores):
#     return f"At match {teams[0]} - {teams[1]}, {'teams played draw.' if scores[0] == scores[1] else teams[scores.index(max(scores))] + ' won!'}"


# other solution
def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        winner = teams[0] + ' won!'
    elif scores[0] < scores[1]:
        winner = teams[1] + ' won!'
    else:
        winner = 'teams played draw.'

    return 'At match ' + teams[0] + ' - ' + teams[1] + ', ' + winner


print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))  # "At match Germany - Ukraine, Germany won!");
print(uefa_euro_2016(['Belgium', 'Italy'], [0, 2]))  # "At match Belgium - Italy, Italy won!")
print(uefa_euro_2016(['Portugal', 'Iceland'], [1, 1]))  # "At match Portugal - Iceland, teams played draw.")
print(uefa_euro_2016(['Albania', 'Switzerland'], [1, 2]))  # "At match Albania - Switzerland, Switzerland won!")
print(uefa_euro_2016(['Republic of Ireland', 'Sweden'], [0, 0]))  # "At match Republic of Ireland - Sweden, teams played draw.")
