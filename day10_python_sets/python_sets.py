# s = {}
#
# print("type of s", s, type(s))
#
# s2 = set()
#
# ls =[] or list()
# t = () or tuple()
# d = {} or dict()

# s = set()
#
# print("s details", s, type(s), id(s), dir(s), s.__sizeof__())
#
# s.add(1)
#
# print("s after add", s, type(s), id(s))
#
# s.add(4)
#
# print("s after add 2nd time", s, type(s), id(s))
#
# s2 = {1,2,2,2,2,4,4,1,99,100,76}
#
# print("s2 details", s2, type(s2), id(s2))
#
# s1 = {1,2,3,4}
#
# s2 = {1,2,3,4,5,6,7,8,9,9,10,10}
# print("s1 details", s1, type(s1), id(s1))
# print("s2 details", s2, type(s2), id(s2))
# s1.update('sreeni') # list extend
#
# print("s1 afer update", s1, type(s1), id(s1))
#
# s1.add('sreeni') # list append
# print("s1 after add", s1, type(s1), id(s1))
#
# s1.pop()
# s1.pop()
# s1.pop()
#
# print("s1 after pop", s1, type(s1), id(s1))
# #
# # s1.remove(999)
#
# s1.discard(999)
#
# print("s1 after remove", s1, type(s1), id(s1))


s1 = {1,2,3,4}
s2 = {4,5,6,7}

# print("s1",s1)
# print("s2",s2)
# print("union", s1.union(s2))
# print("s1 after union",s1)
# print("s2 after union",s2)
# print("intersection", s1.intersection(s2))
print("difference", s1.difference(s2))
# print("difference", s2.difference(s1))
# print("full difference", s1.difference(s2).union(s2.difference(s1)))
print("s1",s1)
print("s2",s2)
print("difference update", s2.difference_update(s1)) # {5,6,7}
print("s1 after difference update",s1)
print("s2 after difference update",s2)

# file/table1 ==> col1,col2,col3,col4
# table2 ==> col1,col2, col3, col4,audit_cols
#
# table1.columns ==> list() ==> set(ls) #  col1,col2,col3,col4
# table2.column==> list() ==>set(ls) # col1,col2, col3, col4,audit_cols
#
# common_cols = list({col1,col2,col3,col4})


# s1 = { 1,2,3,...999,1000}
# s2 = {2,3,4...999,1000}

fs = frozenset({1,2,3,4,4,5,5,6})

print("fs details", fs, type(fs), id(fs), dir(fs))

