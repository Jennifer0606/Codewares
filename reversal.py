"""
reversal X and Y without use temp
"""
string = "XY"
result = ""
for i in string[::-1]:
    result += i

print(result)