# 4 ways of copy

# 1.Reference copy
# 2. copy method
# 3. Shallow copy
# 4 . deep copy

ls1 = [1,2,3]

ls2 = ls1 # Reference copy

# print("ls1", ls1, id(ls1))
# print("ls2", ls2, id(ls2))

# ls2.append(4)
#
# print("ls1 after append", ls1, id(ls1))
# print("ls2 after append", ls2, id(ls2))
#
# ls1.remove(1)
#
# print("ls1 after remove", ls1, id(ls1))
# print("ls2 after remove", ls2, id(ls2))


ls3 = ls1.copy() # separate copy will be created in new memory location

print("ls1 ", ls1, id(ls1))
print("ls2 ", ls2, id(ls2))
print("ls3 ", ls3, id(ls3))

ls1.append(5)

print("ls1 after append", ls1, id(ls1))
print("ls2 after append", ls2, id(ls2))
print("ls3 after append", ls3, id(ls3))

ls3.pop(1)

print("ls1 after pop", ls1, id(ls1))
print("ls2 after pop", ls2, id(ls2))
print("ls3 after pop", ls3, id(ls3))

ls4 = ls2

print("ls1 ", ls1, id(ls1))
print("ls2 ", ls2, id(ls2))
print("ls3 ", ls3, id(ls3))
print("ls4 ", ls4, id(ls4))
