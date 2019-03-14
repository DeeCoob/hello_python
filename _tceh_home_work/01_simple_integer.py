# Напишите программу, которая находит все простые числа между 0 и пользовательским числом

user_number = int(input("Enter you number: "))
user_list = list()


for n in range(2, user_number + 1):  # обойдем все числа от двух до указанно числа
    for m in range(2, n):  # обойдем все от двух до текущего числа
        if n % m == 0:
            break
    else:
        user_list.append(n)

print(user_list)













