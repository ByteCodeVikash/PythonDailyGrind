"""
10. Write a python program to create a function to check whether a string is an anagram
or not.
"""
def check_anagram(s1,s2):
       s1=s1.lower()
       s2=s2.lower()

       if sorted(s1)==sorted(s2):
          print("it is anagram")
       else:
          print("it is not anagram")


s1=input("Enter first string: ")
s2=input("Enter second string: ")
check_anagram(s1,s2)