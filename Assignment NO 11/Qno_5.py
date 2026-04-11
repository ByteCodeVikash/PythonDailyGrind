#5. Write a python script to find next prime number of a given number


num = int(input("Enter number: "))

n = num + 1

while True:

    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print("Next prime number is:", n)
        break

    n = n + 1    
