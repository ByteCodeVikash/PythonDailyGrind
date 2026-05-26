"""
3.Write a function that accepts two dictionaries containing character frequencies. Iterate
through them to merge the counts. If a key exists in both, use a lambda expression in-
side a map operation to determine the higher frequency and store only that value in the
returned dictionary.
"""

def dictfun(D1,D2):
	D3={}

	for key in D1:
		D3[key]=D1[key]

	for key in D2:
	    if key in D3:
	       higher = list(map(lambda x: max(x[0], x[1]),
                              [(D3[key], D2[key])]))[0]


	       D3[key]=higher
	    else:
	    
	        D3[key]=D2[key]

	print(D3)           	




D1={'a':3,'b':2}
D2={'a':7,'c':3}

dictfun(D1,D2)
