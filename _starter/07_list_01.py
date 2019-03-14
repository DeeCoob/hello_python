int_list = [1, 3, 5, 7]
char_list = ['a', 'b', 'x', 'y']
empty_list = []

print("Numbers:", int_list)
print("Chars:", char_list)
print("Empty:", empty_list)

list_from_range = list(range(5))
print("list_from_range =", list_from_range)

list_from_string = list('string')
print("list_from_string =", list_from_string)
print(list_from_string[-1], list_from_string[1])

index = int(input("Enter index:"))
print(list_from_string[index])
