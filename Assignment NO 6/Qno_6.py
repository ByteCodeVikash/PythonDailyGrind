#6. Write a python script to check whether a given number is a three digit number or not.


num=int(input("Enter three digit here: "))

if num>=100 and num<=999:
   print(num,"is three digit.")
else:
   print(num,"is not three digit.")   