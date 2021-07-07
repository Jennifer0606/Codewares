"""
https://www.codewars.com/kata/55cb854deb36f11f130000e1/train/python
Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius.
Unfortunately his code has some bugs.

Find the errors in the code to get the celsius converter working properly.

To convert fahrenheit to celsius:

celsius = (fahrenheit - 32) * (5/9)
Remember that typically temperatures in the current weather conditions are given in whole numbers.
It is possible for temperature sensors to report temperatures with a higher accuracy such as to the nearest tenth.
Instrument error though makes this sort of accuracy unreliable for many types of temperature measuring sensors.
"""


# my solution
def weather_info(temp):
    c = convert_to_celsius(temp)
    return "{} is above freezing temperature".format(c) if c > 0 else "{} is freezing temperature".format(c)


def convert_to_celsius(temperature):
    return (temperature - 32) * (5 / 9)


print(weather_info(50))  # return '10.0 is above freezing temperature'
print(weather_info(23))  # return '-5.0 is freezing temperature'
