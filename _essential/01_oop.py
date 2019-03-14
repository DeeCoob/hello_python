class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)


mike = Person("Mike", 22)
miki = Person("Miki", 18)


mike.print_info()
miki.print_info()

