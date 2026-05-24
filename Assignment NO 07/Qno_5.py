"""
5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
"""

num=int(input("Enter number here: "))

if num%2==0:
   print("Saurabh SHukla.")
elif num%2!=0 and num<0:
   print("Prateek Jain.")
elif num%2!=0 and num>0:
   print("Aditya choudhary.")  
       
