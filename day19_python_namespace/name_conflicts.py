a = 10
def outer_function():
    a=11
    def inner_function():
        a=12
        print("a value is",a)
    inner_function()

outer_function()

# LEGB