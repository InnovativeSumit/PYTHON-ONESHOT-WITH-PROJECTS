num = int(input("Enter a number to print its table: "))

i = 1
print(f"Multiplication table of {num}:")

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
