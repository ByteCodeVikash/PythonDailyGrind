#Write a python script to check whether a given number is Prime or not

num=int(input("Enter a number here: "))

for i in range(2,num):
    if num%i==0:
       print("Not prime")
       break

else:
    print("Prime")                  