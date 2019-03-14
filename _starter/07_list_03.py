int_list = "string"
print("My list consist from", len(int_list), "elements")
while True:
    value = input("Enter a value: ")
    if value in int_list:
        print(value, "is in my list")
    else:
        print(value, "is not in my list")

