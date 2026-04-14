"""
6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class.
"""

class Calculator:

      def __init__(self,num1,num2):
                self.num1=num1
                self.num2=num2


      def adding(self):
                return self.num1+self.num2

      def subtracting(self):
                return self.num1-self.num2

class Calculator2(Calculator):
      def multiplication(self):
                return self.num1*self.num2
      def division(self):
                return self.num1/self.num2                         



num1=int(input("Enter first number here: "))
num2=int(input("Enter second number here: "))

s=Calculator2(num1,num2)
print(s.adding())
print(s.subtracting())
print(s.multiplication())
print(s.division())