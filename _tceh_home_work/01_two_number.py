# Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-".
# В зависимости от знака выводит их сумму или разницу

sign = str(input('Enter "+" or "-": '))
first_number = float(input('Enter first number: '))
second_numbers = float(input('Enter second number: '))

if sign == "+":
    print("Sum of {} and {} is {}".format(first_number, second_numbers, first_number + second_numbers))
elif sign == "-":
    print("Difference of {} and {} is {}".format(first_number, second_numbers, first_number - second_numbers))
else:
    print("Wrong sign")


samething 