class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def salon(self):
        print(self.model, self.number, "is from", self.year)


phone = Phone("ifone", "X", 2018)
phone.printphone()

