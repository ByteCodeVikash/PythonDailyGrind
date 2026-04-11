#👉 Write a python script to print first N even natural numbers

n=int(input("Enter n value here: "))
i=1

while i<n:
     print(i*2)
     i+=1   

#using for loop
n=int(input("Enter n value here: "))

for i in range(1,n+1):
       print(i*2)     