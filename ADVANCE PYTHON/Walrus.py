# without walrus operators
# n = len("Sumit")
# if(n>4):
#     print(n)

# with walrus operators
# if(n:= len("Sumit"))>4:
#           print(n)

# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
# Output: List is too long (5 elements, expected <= 3)