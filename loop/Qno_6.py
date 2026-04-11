#👉 Write a python script to print first N natural numbers in reverse order

n=int(input("Enter n value here: "))

while n:
      print(n)
      n-=1


#using for loop
n=int(input("Enter n value here: "))

for i in range(n,0,-1):
      print(i)