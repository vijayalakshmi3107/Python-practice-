def check_number(a):
    if a > 0:
        return "Positive"
    elif a < 0:
        return "Negative"
    else:
        return "Zero"

a = int(input("Enter a number: "))
print("Number is:", check_number(a))
