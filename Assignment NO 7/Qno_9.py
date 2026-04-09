"""
9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
"""

year = int(input("Enter year: "))

# Determine type
if year % 100 == 0:
    if year % 400 == 0:
        result = "century_leap"
    else:
        result = "century_non_leap"
else:
    if year % 4 == 0:
        result = "non_century_leap"
    else:
        result = "non_century_non_leap"

# Match-case
match result:
    case "non_century_leap":
        print("Non century leap year")
    case "century_leap":
        print("Century leap year")
    case "non_century_non_leap":
        print("Non century non leap year")
    case "century_non_leap":
        print("Century non leap year")