"""
10. Write a python script to check whether a given number is prime or armstrong number
using 2 different threads
"""
import threading

num = int(input("Enter number: "))


def check_prime():
    if num <= 1:
        print("Not Prime")
        return
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return
    print("Prime Number")


def check_armstrong():
    temp = num
    total = 0
    n = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10

    if total == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong")


t1 = threading.Thread(target=check_prime)
t2 = threading.Thread(target=check_armstrong)

t1.start()
t2.start()

t1.join()
t2.join()