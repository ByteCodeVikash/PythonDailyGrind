#Write a python script to create a ValueError




try:
   num1=int(input("Enter a first number here: "))
   num2=int(input("Enter second number here: "))
   print(num1+num2)

except ValueError:
   print("Please enter intger value.")   