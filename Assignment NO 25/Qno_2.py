"""
2. Write a python script to create a user account class with 2 instance variables (userid
and balance). Create 3 user objects and add all the users using operator
overloading.
"""


class UserAccount:
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance

    def __add__(self, other):
        return UserAccount(0, self.balance + other.balance)


u1 = UserAccount(1, 100)
u2 = UserAccount(2, 200)
u3 = UserAccount(3, 500)

result = u1 + u2 + u3
print(result.balance)




