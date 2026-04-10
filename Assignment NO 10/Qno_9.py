"""
Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)
"""

num=int(input("Enter number here: "))

binary=""

for i in range(1,num+1):
         rem=num%2
         binary=str(rem)+binary
         num=num//2

         if num == 0:
            break

print(binary)

