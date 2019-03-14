# Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print()
# выведите на экран прямоугольный треугольник.

n = 5
sim = "*"
s = ""

print(sim)
for i in range(n):
    s = s + " "
    print(sim + s + sim)
    i += i
print(sim * (n + 3))




