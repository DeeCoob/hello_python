x = int(input('First number: '))
y = int(input('Second number: '))
operation = input('Operation: ')

result = None

if operation == '/':
    result = x / y

if result is not None:
    print('Resoult is:', result)

