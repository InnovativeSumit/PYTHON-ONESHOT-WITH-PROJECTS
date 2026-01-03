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


# map() FUNCTION:
# map(function, iterable)
# - It applies a function to each element of the iterable
# - Returns modified elements
# lambda n: n * 2 → doubles each number
doubles = list(map(lambda n: n * 2, evens))
print(doubles)


# reduce() FUNCTION:
# reduce(function, iterable)
# - It reduces the iterable to a single value
# - The function takes two arguments at a time
# Example: (((a+b)+c)+d) ...
sum = reduce(add_all, doubles)
print(sum)


# lambda FUNCTION:
# lambda is an anonymous (nameless) function
# Syntax: lambda arguments : expression
# Used for short, simple operations
# Example used above:
# lambda n: n % 2 == 0  → checks even numbers
# lambda n: n * 2       → doubles the value
