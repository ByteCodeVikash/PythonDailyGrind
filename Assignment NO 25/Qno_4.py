"""
4. Write a python script to create two Threads. First thread will print all Even numbers
and Second thread will print all Odd numbers till 100.
"""

import threading 


def Printeven():
    i=1
    while i<=100:
          if i%2==0:
             print(i,end=",")

          i+=1

def PrintOdd():
       i=1
       while i<100:
             if i%2!=0:
               print(i,end=",")
             i+=1    

t1=threading.Thread(target=Printeven)
t2=threading.Thread(target=PrintOdd)                     

t1.start()
t2.start()

