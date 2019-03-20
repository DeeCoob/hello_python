# *ЗАДАЧА 1:
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person),
# который возвращает знакомы ли два человека


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.user_friendly_list = list()

    def know(self, person):
        self.user_friendly_list.append(person)

    def is_known(self, person):
        if person in self.user_friendly_list:
            print('{} is {} friend'.format(self.name, person.name))


mary = Person(32, 'Mary')
john = Person(19, 'John')

john.know(mary)
john.is_known(mary)
mary.is_known(john)



