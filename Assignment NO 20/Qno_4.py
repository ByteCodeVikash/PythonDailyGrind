#Write a recursive python function to print first N odd natural numbers in reverse order


def PrintEven(n):
    if n>0:
       print(2*n-1)
       PrintEven(n-1)
       


n=int(input("Enter n value here: "))
PrintEven(n)       