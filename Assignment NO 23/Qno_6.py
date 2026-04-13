#6. Write a python program to create 3 user objects and find the youngest of all.

class User:
    
    def __init__(self,age):
        self.age=age





u1=User(age=25)
u2=User(age=35)
u3=User(age=11)


if u1.age<u2.age and u1.age<u3.age:
   print(u1.age,"is youngest")
elif u2.age<u1.age and u2.age<u3.age:
   print(u2.age,"is youngest.")
else:
   print(u3.age,"is youngest")

