class Calc(object):
    def __init__(self, number):
        self.number = number

    def calc_value(self):
        return self.number * 10 - 2

    @staticmethod
    def print_number(value_to_print):
        print('-----')
        print('Number is', value_to_print)
        print('-----')

    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)


class CalcExtraValue(Calc):
    def calc_value(self):
        return self.number / 4


a = Calc(7)
a.calc_and_print()
print()
c = CalcExtraValue(7)
c.calc_and_print()
