rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()  # move to next line


# see this for more 25 patterns : ->
# https://www.wscubetech.com/resources/python/programs/pattern