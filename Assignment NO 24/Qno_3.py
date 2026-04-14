"""
3. Write a python script to update 2nd Question, change email and age to __email and
__age.
"""

class Profile:

      def __init__(self,name,email,age):
                self.name=name
                self.__email=email
                self.__age=age

      def show(self):
                print(self.name)
                print(self.__email)
                print(self.__age)


name=input("Enter your name here: ")
email=input("Enter your email here: ")
age=int(input("Enter your age here: "))

s=Profile(name,email,age)
s.show()


