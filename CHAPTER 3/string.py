s = "PYTHON"
print(len(s))   # Length of string

s = "PYTHON"
print(s[0])     # First character
print(s[-1])    # Last character
print(s[0:3])   # Characters from index 0 to 2
print(s[2:])    # From index 2 to end
print(s[:4])    # From start to index 3
print(s[:])     # Whole string


s = "PYTHON"
print(s[-6:-3])   # From -6 to -4 (PYT)
print(s[-4:])     # Last 4 characters (THON)
print(s[:-2])     # Everything except last 2 chars (PYTH)

s = "PYTHON"
print(s[::2])     # Skip 1 char → PTON
print(s[1::2])    # Start at index 1 → YHN
print(s[::-1])    # Reverse string → NOHTYP
print(s[1:5:2])   # From 1 to 4 with step 2 → YT

s = "HELLOWORLD"

print(s[3:8])     # LOWOR
print(s[-8:-3])   # LLOWO
print(s[2:-2])    # LLOWOR
print(s[::-2])    # Reverse with step → DRWLE

s = "PYTHONPROGRAM"

print("String:", s)
print("Length:", len(s))

print("First 5:", s[:5])
print("Last 5:", s[-5:])
print("Middle part:", s[3:10])
print("Reverse:", s[::-1])
print("Even index chars:", s[::2])
print("Odd index chars:", s[1::2])
