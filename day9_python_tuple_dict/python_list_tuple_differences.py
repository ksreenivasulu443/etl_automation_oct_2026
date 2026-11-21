import timeit

ls = [1,2,3,4,5,6,7,8]
t  = (1,2,3,4,5,6,7,8)

print("ls", ls, type(ls), ls.__sizeof__())

print("t", t, type(t), t.__sizeof__())


ls = [1,2,3,3,3,3,4,5,5,5,5,5,10,10,11,1,1,1,1,1]
t = (1,2,3,3,3,3,4,5,5,5,5,5,10,10,11,1,1,1,1,1)

print(ls.count(1), ls.__sizeof__())

print(t.count(1), t.__sizeof__())

print(t.count(1))

print("time to display count of 1 on list", timeit.timeit(f"{ls}.count(1)", number=10000000))
print("time to display count of 1 on tuple", timeit.timeit(f"{t}.count(1)", number=10000000))