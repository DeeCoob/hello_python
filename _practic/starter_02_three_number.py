# Задание 2
# Напишите программу, которая запрашивает три целых числа a, b и x и выводит True,
# если x лежит между a и b, иначе – False.

while True:
    a = input("Enter a: ")
    b = input("Enter b: ")
    x = input("Enter x: ")

    if a < x < b or a > x > b:
        print(True)
    else:
        print(False)



