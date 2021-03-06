# lists:
not_a_list = (1, 2,)
list1 = [1, 2]
list2 = list(not_a_list)

print(list1 == list2, not_a_list == list1)

list1.append(3)
print('append() returns None: ', list1.append(4))
print(list1)

list1.extend(list2)
print(list1)

list1.insert(1, 'inserted value')
print(list1)

var = ['bar']
new_var = var
var.append('foo')
var[0] = 'baz'
print(new_var)

# delete:
test_list = ['popo', 'remove', 'del']

# by index:
popped = test_list.pop(0)
print('popped value is "{}"'.format(popped))

# by value:
test_list.remove('remove')

# or del it:
del test_list[0]

# multi-dimensional list:
multi = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]
for row in multi:
    print(row)
    for element in row:
        print('element: ', element)
