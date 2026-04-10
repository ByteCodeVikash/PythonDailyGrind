"""
10. Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)
"""

num=int(input("Enter numbere here: "))

octal=""

for i in range(1,num+1):
      rem=num%8
      octal=str(rem)+octal
      num=num//8

      if num==0:
         break

print(octal)         