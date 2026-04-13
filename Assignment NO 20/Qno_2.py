#Write a recursive python function to print first N natural numbers in reverse order


def PrintN(n):
    if n>0:
       print(n)
       PrintN(n-1)


n=int(input("Enter n value here: "))
PrintN(n)