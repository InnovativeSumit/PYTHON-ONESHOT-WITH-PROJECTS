num = int(input("Enter a number to print its table: "))
n = int(input("Enter up to which number you want the table: "))

print(f"Multiplication table of {num} in reverse order:")

for i in range(1, n+1):
    print(num, "x",(n+1- i), "=", (num *(n+1-i)))
