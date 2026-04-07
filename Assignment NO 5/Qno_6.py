"""
6. Write a python script which takes a three digit number from the user and displays
only its middle digit.
"""

num=int(input("Enter three digit here: "))

output=(num//10)%10

print(output)