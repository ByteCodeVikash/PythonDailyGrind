#1. Write a python program to create a user class with 3 properties : name, age, email.

class user:
      def __init__(self,name,age,email):
          self.name=name
          self.age=age
          self.email=email



s=user(name='vikash',age=25,email='vikash@gmail.com')
print(s.name,s.age,s.email)         