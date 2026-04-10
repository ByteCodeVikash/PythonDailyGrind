#Write a python script to calculate sum of digits of a given number.

num=int(input("Enter number here: "))

total=0

for i in str(num):
	total=total+int(i)

print(total)

	
