"""
2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.
"""

def check_prime(num):
      for i in range(2,num):
          if i%2==1:
             print("This is not prime.")
             break
      else:
           print("this is prime.")

num=int(input("Enter a number here: "))
check_prime(num)
