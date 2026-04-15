#5. Write a python script to create 2 threads to add all the values from 1 to 100.
import threading

sum1 = 0
sum2 = 0

def part1():
    global sum1
    for i in range(1, 51):
        sum1 += i

def part2():
    global sum2
    for i in range(51, 101):
        sum2 += i


t1 = threading.Thread(target=part1)
t2 = threading.Thread(target=part2)

t1.start()
t2.start()

t1.join()
t2.join()

total = sum1 + sum2
print("Total sum:", total)