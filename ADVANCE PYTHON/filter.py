from functools import reduce   # reduce() is imported from functools module

num = [2, 3, 4, 4, 5, 56, 7]

def add_all(a, b):
    # This function takes two values and returns their sum
    # reduce() will repeatedly use this function to combine values
    return a + b


# filter() FUNCTION:
# filter(function, iterable)
# - It filters elements from the iterable based on a condition
# - The function must return True or False
# - Only elements returning True are kept
# lambda n: n % 2 == 0  → checks if a number is even
evens = list(filter(lambda n: n % 2 == 0, num))
print(evens)