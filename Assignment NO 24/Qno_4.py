"""
4. Write a python script to update 2nd Question, add a class variable (platform) and
create a classmethod to access it.
"""

class Profile:

      platform="school"


      def __init__(self,name,email,age):
          self.name=name
          self.__email=email
          self.__age=age

      def show(self):
          print(self.name)
          print(self.__email)
          print(self.__age)

      @classmethod
      def showplatfrom(cls):
          print(cls.platform)    

name=input("Enter name here: ")
email=input("Enter email here: ")
age=int(input("Enter age here: "))

s=Profile(name,email,age)
s.show()  
Profile.showplatfrom()            