"""
Write a python program to check whether a given number is positive, negative or
zero using match case statement
"""

num=int(input("Enter number here: "))

if num>0:
   Result="positive"
elif num<0:
   Result="negative"
else:
   Result="Zero"                        	
           

match Result:
      
      case "positive":
            print("positive.")
      case "negative":
            print("negative")
      case "Zero":
            print("Zero.")                       
               