def add():
    print("addition")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a + b)

def sub():
    print("subtraction")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a - b)

def mul():
    print("multiplication")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a * b)

def div():
    print("division")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))  
    if b == 0:                    
        print("Cannot divide by zero")
    else:
        print(a / b)


add()
sub()
div()
mul()
