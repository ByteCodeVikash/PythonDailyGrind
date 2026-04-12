"""
1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements.
"""

def show(l1):
    print(list(set(l1)))



l1=[1,2,3,4,5,1,1,1,2,3,4]
show(l1)    