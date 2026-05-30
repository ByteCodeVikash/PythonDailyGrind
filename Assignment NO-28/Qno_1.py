"""
Write a function using reduce() to iterate over a list of strings and return a single concate-
nated string containing only the characters that appeared exactly once across the entire
collection.
"""

from functools import reduce

def func(s):
	result=reduce(lambda a,b:a+b,s)

	feq={}
	for i in result:
		if i in feq:
		     feq[i]=feq[i]+1
		else:
		     feq[i]=1  

	# lowest_values=min(feq.values())
	lowest=[]
	
	for  chara,scores in feq.items():
		if scores==1:
			lowest.append(chara)	
	final_result=reduce(lambda a,b:a+b,lowest)
	return final_result



s=["vikash","shivam","jalaj"]
print(func(s))