"""
https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python
Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries.
Marketing thinks it would be great to welcome visitors to the site in their own language.
Luckily you already use an API that detects the user's location, so this is an easy win.

The Task
Think of a way to store the languages as a database (eg an object).
The languages are listed below so you can copy and paste!
Write a 'welcome' function that takes a parameter 'language' (always a string),
and returns a greeting - if you have it in your database.
It should default to English if the language is not in the database, or in the event of an invalid input.
"""


# my solution
def greet(language):
    database = {'english': 'Welcome',
                'czech': 'Vitejte',
                'danish': 'Velkomst',
                'dutch': 'Welkom',
                'estonian': 'Tere tulemast',
                'finnish': 'Tervetuloa',
                'flemish': 'Welgekomen',
                'french': 'Bienvenue',
                'german': 'Willkommen',
                'irish': 'Failte',
                'italian': 'Benvenuto',
                'latvian': 'Gaidits',
                'lithuanian': 'Laukiamas',
                'polish': 'Witamy',
                'spanish': 'Bienvenido',
                'swedish': 'Valkommen',
                'welsh': 'Croeso'}
    # for a, b in database.items():
    #     if language == a:
    #         return b
    #
    # return "Welcome"

# other solution
    try:
        return database[language]
    except:
        return 'Welcome'


# best soultion
# def greet(language):
#     return {
#         'czech': 'Vitejte',
#         'danish': 'Velkomst',
#         'dutch': 'Welkom',
#         'english': 'Welcome',
#         'estonian': 'Tere tulemast',
#         'finnish': 'Tervetuloa',
#         'flemish': 'Welgekomen',
#         'french': 'Bienvenue',
#         'german': 'Willkommen',
#         'irish': 'Failte',
#         'italian': 'Benvenuto',
#         'latvian': 'Gaidits',
#         'lithuanian': 'Laukiamas',
#         'polish': 'Witamy',
#         'spanish': 'Bienvenido',
#         'swedish': 'Valkommen',
#         'welsh': 'Croeso'
#     }.get(language, 'Welcome')


# other solution
# db = {
# 'english': 'Welcome',
# 'czech': 'Vitejte',
# 'danish': 'Velkomst',
# 'dutch': 'Welkom',
# 'estonian': 'Tere tulemast',
# 'finnish': 'Tervetuloa',
# 'flemish': 'Welgekomen',
# 'french': 'Bienvenue',
# 'german': 'Willkommen',
# 'irish': 'Failte',
# 'italian': 'Benvenuto',
# 'latvian': 'Gaidits',
# 'lithuanian': 'Laukiamas',
# 'polish': 'Witamy',
# 'spanish': 'Bienvenido',
# 'swedish': 'Valkommen',
# 'welsh': 'Croeso'}
#
# def greet(language):
#     return db.get(language, "Welcome")


print(greet('english'))  # return 'Welcome'
print(greet('dutch'))  # return 'Welkom'
print(greet('IP_ADDRESS_INVALID'))  # return 'Welcome'
print(greet(''))  # return 'Welcome'
print(greet(2))  # return 'Welcome'
