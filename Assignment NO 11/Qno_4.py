"""
Write a python script to print all Prime numbers between two given numbers (both
values inclusive)
"""

num1=int(input("Enter first number here: "))
num2=int(input("Enter second number here: "))

for num in range(num1,num2):
    for i in range(num1,num):
          if (num2%i==0):
             break
          else:
             print(num,end=",")  