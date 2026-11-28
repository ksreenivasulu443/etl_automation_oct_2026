k = 10
l = 15

def greeting(name, age):
    print(f"Hello {name}, you are {age} years old.")
    l = 200
    print("l value within greeting function is", l)
    print("within function", locals())

print(greeting(name = 'Sreeni', age=20))
print("gloabls outside of function ", globals())
print("locals() outside of function", locals())
print("l value outside of function", l)

# gloabls -->k,l,greeting
# locals --> name, age, l