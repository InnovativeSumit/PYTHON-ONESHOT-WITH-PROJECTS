# Creating Tuples
t = (1, 2, 3, 4, 5)
print("Original Tuple:", t)

# Accessing Elements
print("First element:", t[0])
print("Last element:", t[-1])
print("Slicing t[1:4]:", t[1:4])
print("Step slicing t[::2]:", t[::2])

# Tuples are immutable – we can't update
print("Tuples are immutable, no direct update allowed")

# Concatenation
t1 = (10, 20, 30)
t2 = (40, 50)
print("Concatenated:", t1 + t2)

# Repetition
print("Repetition:", t1 * 3)

# Length
print("Length:", len(t))

# Count occurrences
t3 = (1, 2, 2, 3, 2, 4)
print("Count of 2:", t3.count(2))

# Index
print("Index of 3 in t3:", t3.index(3))

# Membership
print("Is 4 in tuple?", 4 in t)
print("Is 100 not in tuple?", 100 not in t)

# Tuple Packing
packed = 10, 20, 30
print("Packed tuple:", packed)

# Tuple Unpacking
a, b, c = packed
print("Unpacked a:", a)
print("Unpacked b:", b)
print("Unpacked c:", c)

# Nested Tuple
nested = (1, (2, 3), (4, 5))
print("Nested tuple:", nested)

# Looping
print("Looping through tuple:")
for x in (10, 20, 30):
    print(x)

# Converting list to tuple
lst = [1, 2, 3]
print("List:", lst)
converted = tuple(lst)
print("Converted to tuple:", converted)

# Converting tuple to list
print("Tuple converted to list:", list(t))

# max, min, sum
num_t = (5, 10, 15)
print("Max:", max(num_t))
print("Min:", min(num_t))
print("Sum:", sum(num_t))
