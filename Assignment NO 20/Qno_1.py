#Write a recursive python function to print first N natural numbers.

def PrintN(n):
   
    if n>0:
       PrintN(n-1)
       print(n)


n=int(input("Enter number here: "))
PrintN(n)       