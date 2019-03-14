# Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).
while True:
    a = int(input("Enter number one: "))
    b = int(input("Enter number two: "))
    s = 0

    for i in range(a, b + 1):
        s = s + i

    print("Sum from {} till {} is {}".format(a, b, s))





