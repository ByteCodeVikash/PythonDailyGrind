"""
1.Write a function that accepts a list of strings and uses a loop to filter out any string that
does not contain at least two vowels. Return a dictionary where the keys are the valid
strings and the values are their exact character lengths.
"""

def fun(Slist):
    mydict={}
    vovels="aeiouAEIOU"

    for word in Slist:

       vovels_count=0
       for char in word:
           if char in vovels:
              vovels_count +=1


       if vovels_count >= 2:
          mydict[word]=len(word)
    return mydict       	


Slist=['vikash','shivam','jalaj','nikhil']
print(fun(Slist))
