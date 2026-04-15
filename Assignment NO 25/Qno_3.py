"""
3. Write a python script to create a to print the above user account object using operator
overloading (hint __str__ method).
"""

class UserAccount:

      def __init__(self,userid,balance):
                self.userid=userid
                self.balance=balance

      def __add__(self,other):
          return UserAccount(0,self.balance+other.balance)

      def __sr__(self):
          return f"userid{self.userid},balance:{self.balance}"    


u1=UserAccount(1,110)
u2=UserAccount(2,220)
u3=UserAccount(3,330)

r=u1+u2+u3
print(r.balance)                    
