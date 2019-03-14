def first_function(x):
    return x + 10


print(first_function(10))


def second(x, y):
    print(x + y)


second(1, 3)


def with_default(name = "Nikita"):
    print("Hello", name)


with_default()
with_default("Stas")


def with_many(pos, default_arg = 'some'):
    print(pos, default_arg)


with_many(9)


# many params set
def sum_all(*numbers):
    print(numbers, type(numbers))
    res = 0
    for i in numbers:
        res = res + i
    return res


print(sum_all(1, 12, 44))


# any keywords
def any_keywords(**kwargs):
    print(kwargs, type(kwargs))

print(any_keywords(a = 1, b = 2,c = 3))