def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


while True:
    number = input("Any string: ")
    if is_number(number):
        number = int(number)
        print("Binary is:", bin(number))
        print("Octal is:", oct(number))
        print("Hex is:", hex(number))
    else:
        print("Error: Enter an integer")
        print(type(number))




