class Car:
    pass


c = Car()
print(c, type(c))
print()


# Classes can have variables called fields

class Room:
    number = 'Room 34'
    floor = 4


r = Room()
r1 = Room()
print(r.number, r1.number)
print(r.floor, r1.floor)
print()


# You can modify values:

r.number = 12
r.floor = '5 floor'
print(r.number, r1.number)
print(r.floor, r1.floor)
print()


# Classes can have functions inside: it called a met

class Door:
    def open(self):  # note that 'self' is the object
        print('self is', self)
        print('Door is opened')
        self.opened = True


d = Door()
d.open()
print()


# Methods can accept params

class Terminal:
    def hello(self, user_name):
        print('Hello', user_name)


t = Terminal()
t.hello('Stas')
print()


class Terminal:
    def __init__(self, user_name):
        print('Hello', user_name)


t = Terminal('Stas')
t1 = Terminal('Sasha')
print()


# Classes can have both methods and fields

class Window:
    is_opened = False

    def open(self):
        self.is_opened = not self.is_opened
        print('Window is now', self.is_opened)
        print()


w = Window()
w1 = Window()

print('Initial state', w.is_opened, w1.is_opened)

w.open()
print('New state', w.is_opened, w1.is_opened)





