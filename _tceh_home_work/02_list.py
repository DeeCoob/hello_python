# Создать лист из 6 любых чисел. Отсортировать его по возрастанию

new_list = [1, 2, 17, 7, 7, 8]
new_list.sort()
print(new_list)
print(type(new_list))


# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'

my_list = ['Earth', 'Russia', 'Moscow']
print('{} -> {} -> {}'.format(my_list[0], my_list[1], my_list[2]))


# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

super_list = [1, 2, 17, 7, 'text', 'text']

for i in super_list:
    print(i, super_list.index(i))


# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

for_del_list = ['to-delete', 'to-delete', 'to-delete', '17', 34, (1, 2, 3)]

# by index:
popped = for_del_list.pop(0)
print('popped value is "{}"'.format(popped))

# by value:
for_del_list.remove('to-delete')

# or del it:
del for_del_list[0]

print(for_del_list)


# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

for i in range(10, 0, -1):
    print(i)








