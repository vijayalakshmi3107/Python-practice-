num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

option = int(input("Choose an option (1-4): "))

if option == 1:
    print("Result =", num1 + num2)

elif option == 2:
    print("Result =", num1 - num2)

elif option == 3:
    print("Result =", num1 * num2)

elif option == 4:
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result =", num1 / num2)

else:
    print("Invalid option")
