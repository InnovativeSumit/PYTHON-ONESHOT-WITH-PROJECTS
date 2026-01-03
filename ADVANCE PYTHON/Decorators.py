# DECORATOR FUNCTION
# This decorator ensures that the first argument (a)
# is always greater than or equal to the second argument (b)

def greater_first(func):
    # Wrapper function that modifies the arguments
    def wrap(a, b):
        # If a is smaller than b, swap them
        if a < b:
            a, b = b, a
        
        # Call the original function with modified values
        return func(a, b)
    
    # Return the wrapper function
    return wrap


# Using decorator on subtraction function
@greater_first
def sub(a, b):
    # Returns subtraction of two numbers
    return a - b


# Using decorator on division function
@greater_first
def divide(a, b):
    # Returns division of two numbers
    return a / b


# Calling the decorated functions
result = divide(2, 4)   # Internally becomes divide(4, 2)
print(result)

result_sub = sub(2, 4)  # Internally becomes sub(4, 2)
print(result_sub)
