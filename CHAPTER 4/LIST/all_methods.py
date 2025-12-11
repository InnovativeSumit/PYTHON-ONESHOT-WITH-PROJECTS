# Creating Lists
lst = [1, 2, 3, 4, 5]
print("Original List:", lst)

# Accessing Elements
print("First element:", lst[0])
print("Last element:", lst[-1])
print("Slicing lst[1:4]:", lst[1:4])
print("Step slicing lst[::2]:", lst[::2])
print("Step slicing lst[::2]:", lst[1::3])

# Updating Elements
lst[2] = 100
print("After updating index 2:", lst)
lst[1:3] = [10, 20]
print("After slice update [1:3]:", lst)

# Adding Elements
lst.append(5)
print("After append:", lst)

lst.insert(1, "hello")
print("After insert at index 1:", lst)

lst.extend([60, 70, 80])
print("After extend:", lst)

# Removing Elements
lst.remove(10)
print("After remove 10:", lst)

print("Popped element:", lst.pop(2))
print("After pop index 2:", lst)

print("Popped last element:", lst.pop())
print("After popping last element:", lst)

# Searching
print("Index of 20:", lst[2])
print("Count of 5:", lst.count(5))

# Sorting
num_list = [5, 3, 9, 1, 7]
print("Original num_list:", num_list)

num_list.sort()
print("Sorted ascending:", num_list)

num_list.sort(reverse=True)
print("Sorted descending:", num_list)

# Reversing
lst.reverse()
print("Reversed lst:", lst)

# Copying
copy_list = lst.copy()
print("Copied list:", copy_list)

# Joining Lists
a = [1, 2, 3]
b = [4, 5, 6]
print("Concatenated list:", a + b)

a.extend(b)
print("After extend:", a)

# Built-in Functions
numbers = [10, 20, 30, 40]
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

# Looping
print("Looping through list:")
for x in [1, 2, 3]:
    print(x)

# List Comprehension
squares = [x*x for x in range(5)]
print("Squares using list comprehension:", squares)

# Membership
print("Is 3 in lst?", 3 in lst)
print("Is 100 not in lst?", 100 not in lst)

# Nested List
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print("Nested List (Matrix):", matrix)

# Clearing List
lst.clear()
print("After clear lst:", lst)
