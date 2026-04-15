#6. Write a python script to create 5 threads to fill a list with random numbers till 100.

import threading
import random

numbers = []
lock = threading.Lock()

def fill_list():
    while True:
        lock.acquire()
        if len(numbers) >= 100:
            lock.release()
            break
        num = random.randint(1, 1000)
        numbers.append(num)
        lock.release()


threads = []

for i in range(5):
    t = threading.Thread(target=fill_list)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Total numbers:", len(numbers))
print(numbers)