# Факториалом числа n называется число 𝑛!=1∙2∙3∙…∙𝑛.
# Создайте программу, которая вычисляет факториал введённого пользователем числа.

while True:
    n = int(input("Enter n: "))
    f = 1
    for i in range(n):
        f = f * (i + 1)

    print("Factorial from n is", f)


