"""
4.Implement a generator function that takes a starting integer and yields the next number
in a sequence where even numbers are halved and odd numbers are multiplied by three
and incremented by one. The generator should stop when it reaches the number one.
"""

def collatz(n):
    
    
    while n != 1:
        yield n                    
        
        if n % 2 == 0:             
            n = n // 2             
        else:                      
            n = 3 * n + 1          
    
    yield 1    



start = int(input("Starting number : "))


gen = collatz(start)


for number in gen:
    print(number)
