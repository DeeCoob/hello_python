number = 0
count = 0
while number <= 0:
    number = int(input("Enter positive integer: "))
    count += 1
    print("Try number", count)
    if count == 3:
        print("Try is done, exiting...")
        exit()
print("You entered number", number)
