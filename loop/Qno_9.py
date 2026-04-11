#👉 Write a python script to print all prime numbers between two given numbers (both inclusive)


start=int(input("Enter start number here: "))
end=int(input("Enter end number here: "))

for i in range(start, end+1):

    if i <= 1:
        continue

    for e in range(2, i):
        if i % e == 0:
            break
    else:
        print(i, end=" ")     