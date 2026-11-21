import copy
# ls1 = [[1,2], [3,4]] # nested list inner object [1,2], [3,4]
# ls2 = copy.deepcopy(ls1) # deep copy
# print("ls1 details", ls1, id(ls1), id(ls1[0]), id(ls1[1]))
# print("ls2 details", ls2, id(ls2),id(ls2[0]), id(ls2[1]))
# ls2[0][0] = 999
# print("ls1 details after update", ls1, id(ls1), id(ls1[0]), id(ls1[1]))
# print("ls2 details after update", ls2, id(ls2),id(ls2[0]), id(ls2[1]))
import copy
original = {
    "id": 101,
    "name": "John",
    "marks": {
        "python": 80,
        "sql": 90
    }
}

a = {
    "id": 101,
    "marks": {"python": 80}
}

b = copy.copy(a)
c = copy.deepcopy(a)

print("a details:", a, id(a), id(a['marks'])) # original dict
print("b details:", b, id(b), id(b['marks'])) # shallow copy
print("c details:", c, id(c), id(c['marks']))
#
# print(a["marks"] is b["marks"])
#
# print(a is c)
# print(a["marks"] is c["marks"])