"""9. Write a python program to create a function to check whether a number falls in a
given range."""

def check_num(num,start,end):
          if start <= num <= end:
             print("True")    
          else:
             print("False.")


num=int(input("Enter number here: "))
start=int(input("Enter start number here: "))
end=int(input("Enter end number here: "))
check_num(num,start,end)
