with open("filter.py", "r") as f:
    obj=f.read()

num = "evens"
obj = obj.replace("hello",num)

with open("filter.py", "w") as f:
    c1=(f.write(obj))
    print(c1)