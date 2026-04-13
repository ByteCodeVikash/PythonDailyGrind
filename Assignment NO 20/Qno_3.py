#Write a recursive python function to print first N odd natural numbers

def PrintOdd(n):
    if n>0:
       PrintOdd(n-1)
       print(2*n-1)


n=int(input("Enter n value here:"))
PrintOdd(n)

