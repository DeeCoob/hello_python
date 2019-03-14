# Task 4 Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами
# вводим два числа типа int так как должны быть кратны 5

first = int(input("Enter first numbers: "))
second = int(input("Enter second numbers: "))
user_list = list()

for i in range(first, second):
    if i % 5 == 0:
        user_list.append(i)

print(user_list)


