a = 10 # globals
def outer_function():

    a = 100 # local but it is within the enclosed space
    print("globals inside outer function", globals())
    print("locals inside outer function", locals())

    def inner_function():

        a = 200 # local variable
        print("a value in enclosed space ",a)
        print("globals inside inner function", globals())
        print("locals inside inner function", locals())
    inner_function()

    print("a value in enclosed space ", a)

print("globals outside outer function", globals())
print("locals outside outer function", locals())



print(outer_function())