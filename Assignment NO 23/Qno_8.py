"""
8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size.
"""

class Laptop:
     
      def __init__(self,ram):
          self.brand='hp'
          self.ram=ram
          self.cpu='i7'
          self.hdd='1tb'

      def showConfig(self):
          print(self.brand)
          print(self.ram)
          print(self.cpu)
          print(self.hdd)

l1=Laptop(ram=8)
l2=Laptop(ram=4)
l3=Laptop(ram=16)
list = [l1, l2, l3]

sorted_list = sorted(list, key=lambda x: x.ram)
for i in sorted_list:
    print(i.ram)
