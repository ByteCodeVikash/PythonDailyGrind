#5. Write a python program to delete the age property of the user.

class User:
   
    def __init__(self):
        self.name="Vikash"
        self.age=25

    def show(self):
        del self.age
        print(self.name)


s=User()
s.show()            