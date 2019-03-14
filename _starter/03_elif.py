x = float(input("Enter x: "))
if 0 < x < 10:
    print("Value is in range")
    y = x ** 2 + 2 * x - 3
    if y < 0:
        print("y = ", y, "; y is negative")
    elif y > 0:
        print("y = ", y, "; y is positive")
    else:
        print("y = 0")

