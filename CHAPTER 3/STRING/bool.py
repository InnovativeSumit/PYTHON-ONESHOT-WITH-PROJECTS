s = "Python123"
s1 = "python"
print(s.isalpha())   # Only alphabets?
print(s1.isalpha())   # Only alphabets?

s = "Python123"
s1 = "90662"
print(s.isdigit())   # Only digits?
print(s1.isdigit())   # Only digits?

s = "Python123"
s1 = "90662"
s2 = "python"
print(s.isalnum())   # Alphabets + digits?
print(s1.isalnum())   # Alphabets + digits?
print(s2.isalnum())   # Alphabets + digits?

s = "Python123"
s1 = "PYTHON"
s2 = "python"
s3 = "python123"
print(s.islower())   # All lowercase?
print(s1.islower())   # All lowercase?
print(s2.islower())   # All lowercase?
print(s3.islower())   # All lowercase?


s = "Python123"
s1 = "PYTHON"
s2 = "python"
s3 = "PYTHON123"
print(s.isupper())   # All uppercase?
print(s1.isupper())   # All uppercase?
print(s2.isupper())   # All uppercase?
print(s3.isupper())   # All uppercase?

s = "   "
s1 = "Hello  "  
s2 = "  Hello"
s3 = "  Hello  "
print(s.isspace())   # Only spaces?
print(s1.isspace())   # Only spaces?
print(s2.isspace())   # Only spaces?
print(s3.isspace())   # Only spaces?

print("Hello World".istitle()) # Title case?
