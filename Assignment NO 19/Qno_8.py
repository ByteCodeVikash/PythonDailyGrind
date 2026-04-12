"""
8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.
"""

def lenString(string):
    Upstring=[]
    Lowerstring=[]

    for i in string:
        if i.isupper():
           Upstring.append(i)	
        if i.islower():
           Lowerstring.append(i)   

    print(Upstring)
    print(Lowerstring)    



string=input("Enter string here: ")
lenString(string)