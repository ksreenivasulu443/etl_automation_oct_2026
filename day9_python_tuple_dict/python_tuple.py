t1 = () # Empty lisr
t2 = tuple() # empty list

print("t1 tuple details", t1, type(t1), id(t1), dir(t1), t1.__sizeof__())
print("t2 tuple details", t2, type(t2), id(t2), dir(t2), t2.__sizeof__())


t = (1,2,2,2,3,3,3,35,4,6,7,9)

print("t tuple details", t, type(t), id(t), dir(t), t.__sizeof__())

print("count/occurance 2", t.count(2))

print("count/occurance 4", t.count(4))

print("index of 9", t.index(9))

str2 = 'sreeni'

print("str2 before lower", str2, id(str2)) #123
str2 = str2.lower() # 'sreeni'
print("str2 after lower", str2, id(str2)) #123
str2 = str2.upper() #'SREENI'
print("str2 before upper", str2, id(str2)) #124












