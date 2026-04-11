#👉 Write a python script to print first N odd natural numbers

n=int(input("Enter n value here: "))
i=1
while i<=n:
    print(2*i-1)
    i+=1

#using for loop
n=int(input("Enter n value here: "))
for i in range(1,n+1):
    print(2*i-1,end=" ")    