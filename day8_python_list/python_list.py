"""
doc str
"""
# import sys
#
# ls = [] # empty list
#
# print("details of ls ", ls, type(ls), id(ls),sys.getsizeof(ls) , dir(ls) )
#
# ls2 = list()
#
# print("details of ls2 ", ls2, type(ls2), id(ls2),sys.getsizeof(ls2) , dir(ls2) )
#
#
# ls3 = [ 1,1.2,True, 1+2j, 'ETL',1, True]
# # we are storing diff datatypes data # list can store heterogenuos elements
# # List also accepts duplicate elements
# # order is preserved
#
# ls4 = [1.1,2.2,3.3,4.5,5.1,6.2]
#
# print("details of ls3 ", ls3, type(ls3), id(ls3),sys.getsizeof(ls3) , dir(ls3) )


# ls = [1,2,3]
#
# print("details of ls ", ls, id(ls), dir(ls))
#
# # Mutable and Immutable
#
# ls.append(4)
#
# print("details of ls after append ", ls, id(ls), dir(ls))
#
# ls.pop(0)
# print("details of ls after pop ", ls, id(ls), dir(ls))


# ls = [1,2,3]
#
# print("details of ls ", ls, id(ls), dir(ls))
#
# ls.append(4)
# ls.append(5)
# ls.append(['automation','labs'])
# ls.append([4,5,6,6,7,7])
#
#
# print("details of ls append ", ls, id(ls), dir(ls))

# Extend method

# ls = [1,2,3]
# print("ls details before extend", ls, id(ls))
#
# ls.extend([5,6,7])

# print("details of ls extend ", ls, id(ls))
#
# ls.extend('etl')
# print("details of ls extend ", ls, id(ls))

ls =[1,2,4,5,6,7,8,2]
print("ls details before extend", ls, id(ls))
#
# ls.insert(20,999)
# # ls.insert(-20,999)
#
# print("ls[0]", ls[0])
#
# print("ls[-20]", ls[-20])

# ls.remove(2)# 2 value
#
# ls.remove(8) # 8 value

ls.pop(3)# 3 is index

# ls.clear()

print("ls after clear", ls)


ls3 = [1,5,7,2,0,99,87,101,'etl','automation']

print("ls details before sort", ls3)
# ls3.sort(reverse=True)

ls3.reverse()

print("ls details after reverse", ls3)


t = frozenset({1,2,3})

print("t", t, dir(t))

d = {1:2}

print("d", d, dir(d))