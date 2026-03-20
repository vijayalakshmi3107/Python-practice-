a = []

print("Enter numbers:")

for i in range(1, 6):
    n = int(input("Enter number " + str(i) + ": "))
    a.append(n)

for i in a:
    print(i * i * i)
