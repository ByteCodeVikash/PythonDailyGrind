"""
Write a Python script to print distinct elements along with their frequencies of
occurrence in the list.
"""

mylist=[1,2,3,4,5,2,4,1,1,2,4,7]
thislist=[]

for i in mylist:
    if i not in thislist:
       thislist.append(i)

print(thislist)       
