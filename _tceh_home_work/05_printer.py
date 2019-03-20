# *ЗАДАЧА 2:
# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *


class Printer(object):
    def __init__(self):
        self.values = []

    def log(self, *values):
        self.values = [v for v in values]
        print(self.values)


class FormattedPrinter(Printer):
    def is_print(self, *values):
        print('**************')
        self.log(*values)
        print('**************')


form_text = FormattedPrinter()
form_text.is_print(3, 5, 7)
