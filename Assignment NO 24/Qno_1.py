#1. Write a python script to create a Profile class with 3 attributes (name, email, age).

class Profile:
      
      def __init__(self,name,email,age):
          self.name=name
          self.email=email
          self.age=age


      def show(self):
     	 print(self.name)
     	 print(self.email)
     	 print(self.age)




name=input("Enter your name here: ")
email=input("Enter your email here: ")
age=int(input("Enter your age here: "))

s=Profile(name,email,age) 
s.show()