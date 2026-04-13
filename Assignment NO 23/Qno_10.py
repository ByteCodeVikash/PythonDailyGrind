"""
10. Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values
"""

class Employee:
      def __init__(self,empid,name,salary):
          self.empid=empid
          self.name=name
          self.salary=salary

      def showEmp(self):
         

          print(self.empid)
          print(self.name)
          print(self.salary)


empid=int(input("Enter here empid"))
name=input("Enter name here: ")
salary=int(input("Enter salary: "))
e=Employee(empid,name,salary)
e.showEmp()          

