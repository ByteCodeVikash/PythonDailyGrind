#6. Write a python program to create a function that finds a maximum of four numbers.

def find_num(num1,num2,num3,num4):
            if num1>num2 and num1>num3 and num1>num4:
               print(num1,"is greater number.")
            elif num2>num1 and num2>num3 and num2>num4:
               print(num2,"is greater number.")
            elif num3>num1 and num3>num2 and num3>num4:
               print(num3,"is greater number.")
            else:
               print(num4,"is greater.")

num1=int(input("Enter first number here: "))                        
num2=int(input("Enter second number here: "))
num3=int(input("Enter third number here: "))
num4=int(input("Enter fourth number here: "))

find_num(num1,num2,num3,num4)