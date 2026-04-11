"""
Write a Python script to print indices of all occurrences of a given element in a given
list.
"""

mylist=[1,2,3,4,5,6,7]
element=2

for index,item in enumerate(mylist):
    # print("index:",index,"Item:",item)

    if item==element:
    	print("index:",index,"item:",item)


