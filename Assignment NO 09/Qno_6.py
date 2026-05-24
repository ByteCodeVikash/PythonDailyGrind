#6. Write a python script to print first N even natural numbers

n=int(input("Enter n value here: "))

i = 2
count = 1
while count <= n:
    print(i)
    i += 2
    count += 1