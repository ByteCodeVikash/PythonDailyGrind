#Write a python script to handle the ArithmeticError

a=2
b=0

try:
   print(a/b)
except ArithmeticError:
   print("this is arithmeticerror.")