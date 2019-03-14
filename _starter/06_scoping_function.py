def function():
    global var
    var = "New global variable"
    print(var)


function()
var = "Global variable"
print(var)