# Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).
while True:
    a = int(input("Enter number one: "))
    b = int(input("Enter number two: "))
    s = 0
    i = a

    while a <= i <= b:
        s = s + i
        i = i + 1
        print(s, i)

    print("Sum from {} till {} is {}".format(a, b, s))

