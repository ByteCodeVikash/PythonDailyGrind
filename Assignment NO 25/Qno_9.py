#9. Write a python script to join 2 threads after printing completing the first Question.

import threading
import time

def task1():
    for i in range(5):
        print("Task 1:", i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2:", i)
        time.sleep(1)


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

# wait for both threads
t1.join()
t2.join()

print("Both threads completed")