# **Задачи на закрепление функций:

# 1.Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля,
# возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0


def sum_two_arg(x, y):
    if x > 0 and y > 0:
        result = x + y
    if x < 0 and y < 0:
        result = x - y
    if x * y < 0:
        result = 0
    return result


print(sum_two_arg(-5, -6))


# 2.Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль

def two_max(x, y, z):
    result = [x, y, z]
    result.sort()
    return result[1:3]


print(two_max(-5, -6, 8))


# 3.Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг.
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка,
# если флаг отрицателен - возвращаем новый список с четными числами из входного списка


def lst_bol(l, b):
    tmp_l = []
    if b:
        for i in l:
            if i % 2 == 1:
                tmp_l.append(i)
    else:
        for i in l:
            if i % 2 == 0:
                tmp_l.append(i)
    return tmp_l


print(lst_bol([1, 2, 3, 6, 7, 8, 9], True))

print(lst_bol([2, 3, 4, 5, 6, 7, 8], False))


# **Задачи на закрепление типов аргументов:

# 1.Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба


def n_func(*numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value, min_value


print(n_func(1, 5, 9, 7, 78))


# 2.Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. Е
# сли флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру,
# иначе - к нижнему


def same_function3(same_str, case=True):
    if case:
        new_str = same_str.upper()
    else:
        new_str = same_str.lower()
    return new_str


print(same_function3('Same Text'))
print()
print(same_function3('Same Text', False))
print()
print()


# 3.Написать функцию, которая принимает любое количество позиционных аргументов -
# строк и один парматер по-умолчанию glue, который равен ':'.
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов.
# Для соединения между любых двух строк вставлять glue

def same_function4(*same_str, glue=':'):
    tmp_str = ''
    for i in same_str:
        if len(i) > 3:
            tmp_str = tmp_str + i + glue
    return tmp_str[:-1]


print(same_function4('asdf', 'qwr2', 'zxce'))






