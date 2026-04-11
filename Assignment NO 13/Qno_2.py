#Write a Python script to create a list of first N odd natural numbers.


n=int(input("Enter n value number: "))
l1=[]

for i in range(1,n+1):
      l1.append(2*i-1)

print(l1)      
