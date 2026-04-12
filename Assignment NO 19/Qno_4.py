"""
4. Write a python program to create a function that checks whether a passed string is
palindrome or not.
"""

def check_palindrom(string):
    s = string[::-1]

    if string == s:
        print("This is palindrome")
    else:
        print("This is not palindrome")


string = input("Enter string here: ")
check_palindrom(string)