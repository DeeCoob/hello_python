# Calculator

while True:
    n = input("Enter operation: ")
    if n == "+":
        a = int(input("a = "))
        b = int(input("b = "))
        print("{0} + {1} = {2}".format(a, b, a + b))

    elif n == "-":
        a = int(input("a = "))
        b = int(input("b = "))
        print("{0} - {1} = {2}".format(a, b, a - b))

    elif n == "*":
        a = int(input("a = "))
        b = int(input("b = "))
        print("{0} * {1} = {2}".format(a, b, a * b))

    elif n == "/":
        a = int(input("a = "))
        b = int(input("b = "))
        print("{0} / {1} = {2}".format(a, b, a / b))

    elif n == "**" or n == "^":
        a = int(input("a = "))
        b = int(input("b = "))
        print("{0} ** {1} = {2}".format(a, b, a ** b))

    else:
        print("Error: incorrect operation.")




