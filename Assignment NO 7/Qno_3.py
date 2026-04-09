"""
3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
"""


print("a.isosceles triangle.")
print("b.Right angle triangle.")
print("c.Equilateral triangle.")
print("d.Exit")

choose=input("Enter your menu driven(a-d): ")



match choose:
      case 'a':
           side1=int(input("Enter first side here: "))
           side2=int(input("Enter second side here: "))
           side3=int(input("Enter third side here: ")) 

           if side1==side2 or side1==side3 or side2==side3 :
                   print("isosceles triangle")  
           else:
               print("This is not isosceles triangle")        

      case 'b':
           side1=int(input("Enter first side here: "))
           side2=int(input("Enter second side here: "))
           side3=int(input("Enter third side here: ")) 

           if (side1**2+side2**2==side3**2 or
           	   side2**2+side3**2==side1**2 or
           	   side1**2+side3**2==side2**2):
               print("Right angle triangle")
           else:
               print("it is not right angle triangle.")    



      case "c":
           side1=int(input("Enter first side here: "))
           side2=int(input("Enter second side here: "))
           side3=int(input("Enter third side here: ")) 


           if side1==side2 and side1==side3 and side2==side3:
               print("Equilateral triangle.")
           else:
               print("This is not Equilateral triangle.")
      case 'd':
            print("Exit")   

      case _:
            print("Invalid choice.")              

