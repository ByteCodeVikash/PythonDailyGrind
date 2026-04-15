"""
7. Write a python script to create a clock where 1st thread will print the current time
every second and 2nd will print “1 Minute Completed” after every 1 minute.
"""


import threading
import time

def show_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print("Time:", current_time)
        time.sleep(1)   # 1 second wait

def show_minute():
    while True:
        time.sleep(60)  # 60 seconds wait
        print("1 Minute Completed")


t1 = threading.Thread(target=show_time)
t2 = threading.Thread(target=show_minute)

t1.start()
t2.start()