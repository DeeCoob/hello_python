def my_function():
    print('t')


print(my_function)
print('Functions are object', isinstance(my_function, object))

# You can use variables to store functions

test = my_function
test()

# You can use variables to store functions

my_list = [ ]
my_list.append(my_function)
print(my_list)


# You can pass functions as parameters

def call_passed_function(incoming):
    print('Calling!')
    incoming()
    print('Called!')


call_passed_function(my_function)


# You can not call uncallable things:

try:
    d = 2
    d()  # but you can try
except TypeError as e:
    print('It is not a function', e)


# You can check if something could be called

print(callable(len), callable(45), callable(callable))


# You can return function from a function

def return_min_function():
    return min


test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min value is', min_value)


# Local scope

def scoped_function(arg):
    value = arg * 10
    print(value)


scoped_function(2)
print(scoped_function(2))


def return_some(input_value):
    calc = input_value - 7
    return calc


print()
return_some(2)
print(return_some(2))

SOME_VAR = 'value'

def print_var():
    print(SOME_VAR)


print_var()


def modify_var():
    try:
        SOME_VAR += '_extra'
    except UnboundLocalError as e:
        print('Error', e)


modify_var()
print(SOME_VAR)


GLOBAL_LIST = []


def appand_list(item):
    print('Adding', item)
    GLOBAL_LIST.append(item)

    
appand_list(1)
appand_list(2)
print(GLOBAL_LIST)











