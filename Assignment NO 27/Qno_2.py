"""
2.Create a recursive function that takes a heavily nested list of mixed integers and strings.
The function must flatten the list, extract only the integers, and return their total sum.

"""

def recfun(l1):

	total=0

	for i in l1:
		if type(i) == list:
			total+=recfun(i)
		elif type(i)==int:
		    total+=i	

	return total		



l1=[[1,2,3],['a',9,'c'],[5,'f',6],['a',2,4]]
print(recfun(l1))
