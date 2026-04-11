#Write a Python script to create a list of first N even natural numbers.

n=int(input("Enter n value here: "))
l1=[]

for i in range(1,n+1):
      l1.append(2*i)
print(l1)      