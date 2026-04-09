#1. Write a python script to display the number of days in a given month number.

m=int(input("Enter month number."))

match m:
   case 1:
        print("31")
   case 2:
        print("28/29")
   case 3:
        print("31")
   case 4:
        print("30")
   case 5:
        print("31")
   case 6:
        print("30")
   case 7:
        print("31")
   case 8:
        print("31")
   case 9:
        print("30")
   case 10:
        print("31")
   case 11:
        print("30")
   case 12:
        print("31")
   case  _ :
        print("Please enter valid month number.")                                                           