"""
7. Write a python script to create a Phone class with 2 methods to print the features
(calling and sms).
"""

class Phone:
      def __init__(self):
          self.calling='calling'
          self.sms='sms'

      def show_calling(self):
          return self.calling

      def show_sms(self):
          return self.sms        


s=Phone()
print(s.show_calling())
print(s.show_sms())          