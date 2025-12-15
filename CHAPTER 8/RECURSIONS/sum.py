num = int(input("Enter a number: "))

def sum(n):
    if  n == 1:   # base case
        return 1
    if  n == 0:   # base case
        return 0
    else:
        return n + sum(n - 1)


print("Factorial is:", sum(num))
