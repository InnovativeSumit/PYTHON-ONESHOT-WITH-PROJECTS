# Taking input from user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

def average(a, b, c):
    return (a + b + c) / 3

# Calling the function
avg = average(x, y, z)

print("Average of three numbers is:", avg)
