"""
9. Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).
"""

class Truecaller:
      
      def __init__(self):
          self.contacts={}

      def new_entry(self):
          name=input("Enter your name here: ") 
          number=input("Enter your number here: ")
          self.contacts[number]=name

      def fetch_contact(self):
          number=input("Enter number here: ")
          if number in  self.contacts:
          	        print("Name:",self.contacts[number])
          else:
              print("cannot found")	        


s=Truecaller()
s.new_entry() 
s.new_entry() 
s.fetch_contact()             