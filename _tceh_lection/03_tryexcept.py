try:
    int('str')
except ValueError as e:
    print(e)

try:
    print(1 / 0)
except TypeError:   # тип ошибки, которую ловим
    print("Wrong type!")
except ZeroDivisionError:
    print('/0')

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('Exception! Stop it')
    print(e)

try:
    d = {'key': 23}
    print(d['does not exist'])
except KeyError:
    print("This won't be called")

try:
    print(d['does not exist'])
except KeyError as e:
    print("Got it", e)

try:
    print('try')
except ValueError:
    pass
else:
    print('else')
finally:
    print('finally')

