"""
6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement
"""

word=input("Enter word here: ")

check= " " in word

match check:
      case True:
           print("Multiword")
      case False:
           print("Single word")        