#7. Write a python script to print first N even natural numbers in reverse order

n=int(input("Enter n value here: "))
i = 2*n
while i >= 2:
    print(i)
    i -= 2