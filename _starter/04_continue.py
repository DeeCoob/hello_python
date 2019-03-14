number = 0
while number < 10:
    number += 1
    if 3 < number < 7:
        continue
    print("Current number is:", number, "!", sep='')