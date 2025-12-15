# Taking input from user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

def average():
    avg = (x + y + z) / 3
    return avg   # return the result

# Calling the function
result = average()
print("Average is:", result)
