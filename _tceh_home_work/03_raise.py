# **Задачи на обработку ошибок:

# 1.Пользователь вводит число, если оно четное - выбрасываем исключение ValueError,
# если оно меньше 0 - TypeError, если оно больше 10 - IndexError.
# Обрабатываем ошибку, говорим пользователю, в чем его ошибка

numbers = int(input('Enter you numbers: '))
try:
    if numbers % 2 == 0:
        raise ValueError('number is / 2')
    if numbers < 0:
        raise TypeError('number < 0')
    if numbers > 10:
        raise IndexError('numbers > 10')

except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except IndexError as e:
    print(e)


# 2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта,
# который хочет посмотреть. Если все хорошо - пишите объект в консоль.
# Если нет - обработайте возмозможные ошибки и скажите ему, что не так

my_list = [2, 32, 0, 11]
my_ind = int(input('enter index: '))

print(my_list.pop(my_ind))

