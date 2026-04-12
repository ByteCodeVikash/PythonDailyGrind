"""
9. Write a python program to create a function to check whether a string is a pangram
or not.
"""

def CheckPangram(s):

     s=s.lower()

     for ch in 'abcdefghijklmnpqrstuvwxyz':
         if ch not in s:
            print("Not a pangram")
            return

     print("it is a pangram")     	  





s=input("Enter Stiring here: ")
CheckPangram(s)