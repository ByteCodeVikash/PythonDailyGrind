#Write a Python script to remove all non int values from a list.

l1=[1,'a',2,'b',3,'d']

l2=[]
for i in l1:
	if isinstance(i, int):
		l2.append(i)

print(l2)	



