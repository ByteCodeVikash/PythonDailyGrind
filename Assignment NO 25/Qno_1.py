"""
1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
a class using method overloading.
"""

class Multi:
      
      def multiply(self,*num):
          total=1
          for i in num:
              total=total*i
          return total
          
m=Multi()
print(m.multiply(2,3)) 
print(m.multiply(3,4))
print(m.multiply(2,3,4))             
