"""
8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
Phone Class.
"""

class Calculator:
      def __init__(self,num1,num2):
                  self.num1=num1
                  self.num2=num2

      def adding(self):
          return self.num1+self.num2

      def sub(self):
          return self.num1-self.num2

class Calculator2(Calculator):
      def multi(self):
          return self.num1*self.num2

      def division(self):
          if self.num2==0:
             return "cannot divided by zero." 
          return self.num1/self.num2

class Phone:
      def __init__(self):
          self.calling='calling'
          self.sms='sms'

      def show_calling(self):
          print(self.calling)

      def show_sms(self):
          print(self.sms)

class SmartPhone(Calculator2,Phone):
      def __init__(self,num1,num2):
          Calculator2.__init__(self,num1,num2)
          Phone.__init__(self)       

num1=int(input("Enter first number here: "))
num2=int(input("Enter second number here: "))
s=SmartPhone(num1,num2)

print(s.adding())
print(s.sub())
print(s.multi())
print(s.division())
s.show_calling()
s.show_sms()


          
