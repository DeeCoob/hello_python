# *ЗАДАЧА 1:
# 1. Создать класс корзина, у которого можно выставить разную вместительность для разных объектов.
# В объекты класса корзина можно помещать разные объекты;
# 2. Вам нужно создать класс пакет, в который тоже можно помещать предметы. У него тоже есть вместимость;
# 3. Создать любой класс, объекты которого можно было бы мощешать в корзину и пакет;
# 4. Если вместимости недостаточно, сказать, что объект поместить нельзя.


class Trash(object):
    def __init__(self, size):
        self.size = size

    def put_something(self, something):
        if something.tsize <= self.size:
            print('The trash is small for this')
        else:
            print('In the Trash')


class Package(Trash):

    def put_something(self, something):
        if something.tsize <= self.size:
            print('The Package is small for this')
            print(something.tsize)
            print(something)
        else:
            print('In the Package.')


class Thing(object):
    def __init__(self, tsize):
        self.tsize = tsize


box1 = Trash(30)
bag1 = Package(50)

something1 = Thing(10)
something2 = Thing(30)
something3 = Thing(130)

box1.put_something(something1)
box1.put_something(something2)

bag1.put_something(something2)
bag1.put_something(something3)
