"""
2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division
"""

print("1.Addition.")
print("2.Subtraction.")
print("3.Multiplication.")
print("4.Division.")

chooce=int(input("Enter your chooce (1-4): "))

a=int(input("Enter your first number here: "))
b=int(input("Enter your second number here: "))

if chooce==1:
   print("Result",a+b)
elif chooce==2:
   print("Result",a-b)
elif chooce==3:
   print("Result",a*b)
elif chooce==4:
   print("Reslut",a/b)
else:
   print("Enter valid choose.")   
