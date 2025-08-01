"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    
    if list_one==list_two:
        return 3
    if not list_one:
        return 1
    if not list_two:
        return 2
    str1=""
    str2=""
    for i in list_one:
        str1+=str(i)+','
    for x in list_two:
        str2+=str(x)+','
    if str2 in str1:
        return 2
    if str1 in str2:
        return 1
    return 4