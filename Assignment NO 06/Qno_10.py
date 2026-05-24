"""
10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
"""

num1=int(input("Enter first number here: "))
num2=int(input("Enter second number here: "))
num3=int(input("Enter third number here: "))

if num1>num2 and num1>num3:
   print(num1,"is greater.")
elif num2>num1 and num2>num3:
   print(num2,"is greater.")
else:
   print(num3,"is greater .")      