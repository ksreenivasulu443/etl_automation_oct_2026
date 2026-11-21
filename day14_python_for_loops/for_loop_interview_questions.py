# str1 ='abababacdeef'
# unique_char = set(str1)
#
# print(unique_char)
# # d = {}
# for char in unique_char:
#     print(f"count of {char}", str1.count(char))


str1 ='abababacdeef'
# {'a':4, 'b':3...}
d = {}
for char in str1:
    if char in d:
        d[char] += 1 # d[char] = d[char]+1
    else:
        d[char] = 1 # d.update({char:1})

print("d is", d)
# a4b3c1d1e2f1


output = ''
for key, value in d.items():
    output += key + str(value)

print("output", output)

# sum of n numbers
# sum of squares of n number

print("d.items", d.items())



