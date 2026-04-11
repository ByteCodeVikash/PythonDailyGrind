"""
10. Write a python program to create a function to check whether a given number is even
or odd.
"""

def check_num(num):
     if num%2==0:
        print(num,"Even.")
     else:
        print(num,"odd")

num=int(input("Enter number here: "))
check_num(num)           