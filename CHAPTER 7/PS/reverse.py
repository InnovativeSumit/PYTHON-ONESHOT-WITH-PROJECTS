num = int(input("Enter a number to print its table: "))
print(f"Multiplication table of {num} in reverse order:")

for i in range(1, 11):
    print(num, "x",(11- i), "=", (num *(11-i)))
