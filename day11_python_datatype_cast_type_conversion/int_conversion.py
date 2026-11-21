# input = input("Enter a number: ")
#
# print("input details", input, type(input), len(input))
#
# # input method takes value from the user(console),
# # Always value will be converted to str type
#
# converted_value = int(input)
#
# print("converted_value details", converted_value, type(converted_value))
#
# print(dir('300'))


a = 100
print("a details",a, type(a))

print("a int to int", int(a))
print("a int to float", float(a))
print("a int to str", str(a))
print("a int to bool", bool(a)) # bool(0 or '', None, empty collection type)==> False
# print("a to complex", complex(a))

# print("a int to list", list(a))
print("a to tuple", tuple(a))
