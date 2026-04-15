#8. Write a python script to change the name of the Thread.

import threading

def task():
    print("Running thread")

t = threading.Thread(target=task, name="MyThread")

t.start()