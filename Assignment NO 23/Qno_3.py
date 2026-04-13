"""
3. Write a python program to create 2 objects of the user class and assign different
values
"""

class user:
    
    def __init__(self,num1):
        self.num1=num1
       



s1=user(num1=23)
s2=user(num1=35)
print(s1.num1,s2.num1)        