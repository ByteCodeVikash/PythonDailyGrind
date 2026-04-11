#👉 Write a python script to print all prime numbers between 1 to N

num=int(input("Enter n value here: "))

for i in range(2,num):
    for e in range(2,i):
        if i%e==0:
           break
    else:
           print(i,end=" ")   

