#Write a python script to handle a ValueError

try:
   num1=int(input("Enter first number here: "))
   num2=int(input("Enter second number here: "))
   print(num1+num2)
except ValueError:
   print("Please enter intger value.")   