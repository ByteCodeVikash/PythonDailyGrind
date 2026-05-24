#5. Write a python program to check if all items in the tuple are the same.

t1=(1,1,1,1,1,1,1)
flag=True

for i in t1:
    if i!=t1[0]:

        flag=False
        break

print(flag)    
