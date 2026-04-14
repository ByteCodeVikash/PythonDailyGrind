"""
5. Write a python script to create a Calculator class with 2 methods for adding and
subtracting 2 values.
"""

class Calculator:
      
      def __init__(self,num1,num2):
                self.num1=num1
                self.num2=num2

      def adding(self):
          print(self.num1+self.num2)

      def subtracting(self):
          print(self.num1-self.num2)


num1=int(input("Enter first number here: "))
num2=int(input("Enter second number here: ")) 

s=Calculator(num1,num2)
s.adding()  
s.subtracting()                     