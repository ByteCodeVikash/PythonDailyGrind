"""
9.Implement a function that takes a list of integer tuples. Use a loop and conditional logic
to find and return the tuple that has the highest mathematical product of its internal
elements.
"""

def func(l1):
	max_score=0
	best_result=None

	for i in l1:
		current_score=1

		for number in i:
			current_score=current_score*number

		if current_score>max_score:
		   max_score=current_score
		   best_result=i

	return best_result	   	




l1=[(1,2,3),(2,3),(4,5,1)]
print(func(l1))
