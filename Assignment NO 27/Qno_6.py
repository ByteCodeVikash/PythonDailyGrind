"""
6.Write a function that uses a match-case statement inside a loop to process a list of mixed-
type variables. Append integers to one list, strings to another, and ignore all other types.
Return a tuple of the two resulting lists.
"""

def func(mylist):

	int_list=[]
	str_list=[]

	for item in mylist:
		match item:
			case int():
					int_list.append(item)
			case str():
			        str_list.append(item)

	return(int_list,str_list)
		        

mylist=[1,'a',2.5,'Python',10]
print(func(mylist))			        		