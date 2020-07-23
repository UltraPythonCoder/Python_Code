number = int(input("Choose how many multiplication tables you want: "))
x = 1
while x <= number:
    y = 1
    while y <= 10:
        print(str(x) + " * " + str(y) + " = " + str(x * y))
        y += 1
    x += 1
    print("\t")
