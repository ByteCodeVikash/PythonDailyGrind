"""
9. Write a python program to create a School class and 3 instance variables and 1 class
variable.
"""

class School:

   country='india'	
   def __init__(self):
       self.name='CPS school'
       self.city='delhi'
       self.students=34

   def showSchool(self):
       print(self.name,self.city,self.students)
   @classmethod    
   def showCountry(cls):
       print(cls.country)    


s=School()
s.showSchool()
s.showCountry()