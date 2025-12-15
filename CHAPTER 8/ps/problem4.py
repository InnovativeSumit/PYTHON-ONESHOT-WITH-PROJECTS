rows = int(input("Enter number of rows: "))

def pattern(n):
    if n == 0:      # base case
        return
    pattern(n - 1)
    print("* " * n)



pattern(rows)
