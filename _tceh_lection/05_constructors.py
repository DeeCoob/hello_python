# Constructor is called when new instance is create

class TestClass:
    def __init__(self):
        print('Constructor is called')
        print('Self is the object itself', self)
        print()


t = TestClass()
t1 = TestClass()


# Constructor can have parameters

class Table:
    def __init__(self, numbers_of_legs):
        print('New table has {} legs'.format(numbers_of_legs))


t = Table(4)
t1 = Table(3)
print()


# But we need to save them into the fields!

class Chair:
    wood = 'Same tree'

    def __init__(self, color):
        self.color = color


c = Chair('green')
print(c, c.color, c.wood)

c1 = Chair('Red')
print('variable c did not change!', c.color)
print()



