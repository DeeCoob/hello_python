attemtps_left = 3
while attemtps_left > 0:
    password = input("Enter your password: "
                     "(you have {} attempts left): ".format(attemtps_left))
    attemtps_left -= 1
    if password == "7420241":
        print("Access granted")
        break
else:
    print("Access denied")