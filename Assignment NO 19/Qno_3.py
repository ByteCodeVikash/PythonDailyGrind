"""
3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def check_even(l1):
    l2 = []
    for i in l1:
        if i % 2 == 0:
            l2.append(i)

    print(l2)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
check_even(l1)
