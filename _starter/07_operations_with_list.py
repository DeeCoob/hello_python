my_list = [1, 8 ,5, 3, 9, 0, 0]

# .append обавление элемента в список
my_list.append(17)
print(my_list)

# del удаление элемента из списка
del my_list[:2]
print(my_list)

# изменение элемента списка
my_list[2] = my_list[2] - 14
print(my_list)

for i in my_list:
    print("{} ^ 2 = {}".format(i, i ** 2))





