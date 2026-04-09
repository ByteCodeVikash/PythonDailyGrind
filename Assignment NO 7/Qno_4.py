"""
4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.
"""


age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 10:
    print("Kid")
elif age < 20:
    print("Teen")
elif age < 40:
    print("Young")
elif age < 60:
    print("Experienced")
else:
    print("Senior Citizen")