"""
8.Write a function that accepts a dictionary mapping usernames to a list of integer scores.
Iterate over the dictionary and return a new dictionary where the keys are the usernames
and the values are sets containing only their prime scores.
"""

# Helper function: Prime number check karne ke liye
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main function
def func(D1):
    result = {}
    for key, values in D1.items():
        # List comprehension ki jagah Set comprehension {} ka use kiya gaya hai
        result[key] = {num for num in values if is_prime(num)} 
    return result

D1 = {
    "Aman": [1, 2, 3, 4, 5],
    "Vikash": [11, 12, 13],
    "Shiva": [21, 22, 23]
}

# Final output print karna
print(func(D1))