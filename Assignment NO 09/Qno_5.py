#5. Write a python script to print first N odd natural numbers in reverse order


n=int(input("Enter n value here: "))

i = 2*n - 1
while i >= 1:
    print(i)
    i -= 2