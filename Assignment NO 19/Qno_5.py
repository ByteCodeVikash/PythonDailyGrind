#5. Write a python program to create a function to find the Min of three numbers.

def find_min(a, b, c):
    if a <= b and a <= c:
        print("Min =", a)
    elif b <= a and b <= c:
        print("Min =", b)
    else:
        print("Min =", c)


find_min(10, 5, 8)