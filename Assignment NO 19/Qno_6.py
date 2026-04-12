"""
6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30.
"""

def sqr_list():
    empy_list = []
    i = 1
    while i <= 30:
        empy_list.append(i**2)
        i += 1
    print(empy_list)

sqr_list()         