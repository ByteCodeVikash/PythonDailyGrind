"""
5.Write a decorator function that intercepts the execution of a target function. If the target
function returns a list, the decorator must convert it into a tuple before passing it back to
the caller.
"""

def convert_list_to_tuple(func):
	def wrapper(*args,**kwargs):
		result=func(*args,**kwargs)


		if isinstance(result,list):

			return tuple(result)

		return result
		
	return wrapper
	
@convert_list_to_tuple
def funclist(l1):

	return l1


my_list=[1,2,3,4,5]
output=funclist(my_list)

print("Value returned:", output)
print("Data Type:", type(output))





