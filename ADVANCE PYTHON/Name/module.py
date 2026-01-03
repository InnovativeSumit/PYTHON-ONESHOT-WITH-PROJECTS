def myFunc():
    print("Hello World")
    
myFunc()
print(__name__)

if __name__ == "__main__":
    print("Module is being run directly")
    myFunc()
    print(__name__)