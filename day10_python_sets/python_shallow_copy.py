import copy
#
# ls1 = [1,2,3]
# ls2 = copy.copy(ls1) # shallow copy
# print("ls1 ", ls1, id(ls1))
# print("ls2 ", ls2, id(ls2))
#
#
# ls2.append(4)
#
# print("ls1 after append ", ls1, id(ls1))
# print("ls2 after append ", ls2, id(ls2))
#
# # if list has normal elements( int, str, bool,complex,float, None)
# # No difference between list copy and shallow copy

ls1 = [[1,2], [3,4]] # nested list inner object [1,2], [3,4]

ls2 = copy.copy(ls1) # shallow copy

print("ls1 details", ls1, id(ls1), id(ls1[0]), id(ls1[1]))
print("ls2 details", ls2, id(ls2),id(ls2[0]), id(ls2[1]))

ls2[0][0] = 999


print("ls1 details after update", ls1, id(ls1), id(ls1[0]), id(ls1[1]))
print("ls2 details after update", ls2, id(ls2),id(ls2[0]), id(ls2[1]))

# Outer memories are different and inner object memories are same

ls1.append(500)

print("ls1 details after append", ls1, id(ls1), id(ls1[0]), id(ls1[1]))
print("ls2 details after append", ls2, id(ls2),id(ls2[0]), id(ls2[1]))


d = {1:[1,2,(3,4)], 2""}