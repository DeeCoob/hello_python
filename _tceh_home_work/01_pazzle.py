"""
Задача: реализовать игру в загадки

Требования:
Программа выводить в консоль текст загадки и ждать ввода пользователя
Программа после ввода пользователя ответа должна вывести в консоль результат:
правильный ли ответ дал пользователь
Загадок должно быть 10, тематика вопросов должна быть по первому занятию
Дополнительные требования (со звездочкой или сложные, необязательно для выполнения):
Программа должна в конце игры сказать, сколько ответов дал пользователь: сколько из них было верных
Программа должна не учитывать регистр ответа:
"Python" и "python" оба должны быть правильным ответом на вопрос "Какой язык мы учим?"

"""
all_answers = 0
correct_answers = 0

q1 = "First question? "
a1 = "1"

answer = input(q1)
all_answers += 1

if answer.lower() == a1.lower():
    print("Correct!")
    correct_answers += 1
else:
    print("Incorrect")


q2 = "Second question? "
a2 = "2"

answer = input(q2)
all_answers += 1

if answer.lower() == a2.lower():
    print("Correct!")
    correct_answers += 1
else:
    print("Incorrect")


print("You are correct answer in {} of {}".format(correct_answers, all_answers))

