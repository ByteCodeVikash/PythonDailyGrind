#3. Write a python script to print first M multiples of N.

n=int(input("Enter n value: "))
m=int(input("Enter m value: "))

for i in range(1,m+1):
    print(i*n)