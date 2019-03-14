class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return "Complex ({!r}, {!r})".format(self.real, self.imaginary)

    def __set__(self):
        return "{}{:+d}i".format(self.real, self.imaginary)


Complex(3, 5)