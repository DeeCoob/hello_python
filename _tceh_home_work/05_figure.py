# *ЗАДАЧА 2:
# Пользователь вводит список чисел через пробел. если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, треугольник
# 4 числа, многоугольник
#
# вычисляем периметр и площадь. выводим в консоль.
# можно сделать проверки на "возможность" построить данную фигуру с такими сторонами.


class Figure:
    def __init__(self, user_list):
        self.user_list = user_list.split(' ')
        tmp_list = []
        for i in self.user_list:
            tmp_list.append(float(i))
        self.user_list = tmp_list
        if not 0 < len(self.user_list) < 5:
            raise ValueError('Can not build figure. Out of value!')

    def build(self):
        if len(self.user_list) == 1:
            s = self.user_list[0] ** 2
            p = self.user_list[0] * 4
            result = 'Square is ready: s = {}, p = {}'.format(s, p)

        elif len(self.user_list) == 2:
            s = self.user_list[0] * self.user_list[1]
            p = float(self.user_list[0] + self.user_list[1]) * 24
            result = 'Square is ready: s = {}, p = {}'.format(s, p)

        elif len(self.user_list) == 3:
            if self.user_list[0] + self.user_list[1] > self.user_list[2]:
                p = self.user_list[0] + self.user_list[1] + self.user_list[2]
                s = (p / 2 * (p / 2 - self.user_list[0]) * (p / 2 - self.user_list[1]) *
                     (p / 2 - self.user_list[2])) ** 0.5
                result = 'Square is ready: s = {}, p = {}'.format(s, p)
            else:
                result = 'Can not build triangle.'

        return result


user_value = input('Enter a list: ')
some_shape = Figure(user_value)
print(some_shape.build())







