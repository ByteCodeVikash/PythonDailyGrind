#4. Write a python program to init default values for user object using __init__ method.


class user:
   def __init__(self):
       self.name="vikash"
       self.age=25



s=user()
print(s.name,s.age)       