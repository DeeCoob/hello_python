# Дополнительное задание:
# Для тех, кто решил игру загадки без использования циклов и словарей -
# прошу ради интереса сделать со словарем и циклом,
# посмотрите, насколько удобнее и короче стал ваш код.

all_answers = 0
correct_answers = 0

my_dict = {'How match 5 + 5 ': '5', 'How many "r" in "Errors" ': '3'}

for key, value in my_dict.items():
    answer = input(key)
    all_answers += 1
    if answer == value:
        correct_answers += 1
        print('Correct!')
    else:
        print('Incorrect')

print('Game over')
print("You are correct answer in {} of {}".format(correct_answers, all_answers))
