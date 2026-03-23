a = int(input("enter a num: "))
def factorial(a):
    if a < 0:
        return("not defined by negative numbers")
    
    result = 1
    for i in range(1, a+1):
        result = result*i

    return result
     
print("Factorial =" , factorial(a))
