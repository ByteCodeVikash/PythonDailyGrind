"""
8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
"""

word1=input("Enter first string here: ")
word2=input("Enter second string here: ")

if word1==word2:
   result="equal"
elif word1<word2:
   result="before"
else:
   result="after"

 
match result:
   case "equal":
        print("Identical.")
   case "before":
        print("first String comes before second.")
   case "after":
        print("First string comes after second")                
