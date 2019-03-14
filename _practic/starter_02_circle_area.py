# Вычисление площади круга
while True:
    print("""Area of a circle: 
    1. From radius
    2. From diameter
    3. Exit""")

    var = int(input("Choose your var: "))
    if var == 1:
        r = float(input("Input radius: "))
        s = 3.14 * r ** 2
        print("Area of a circle is", round(s, 2))
        print()

    elif var == 2:
        d = float(input("Input diameter: "))
        s = 3.14 * (d / 2) ** 2
        print("Area of a circle is", round(s, 2))
        print()

    elif var == 3:
        print("The program has been closed.")
        break

    else:
        print("Wrong data! Please, try again.")
        print()



