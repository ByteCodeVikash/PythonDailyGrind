"""
7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values).
"""

class Laptop:
      
      def __init__(self):
          self.brand='hp'
          self.ram='4gb'
          self.cpu='i7'
          self.hdd='1tb'

      def showConfig(self):
          print(self.brand)
          print(self.ram)
          print(self.cpu)
          print(self.hdd)


s=Laptop()
s.showConfig()               