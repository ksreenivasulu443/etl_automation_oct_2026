# d = {}
#
# d2 = dict()
#
# print("d details", d, type(d),id(d), dir(d))
#
# print("d2 details", d2, type(d2),id(d2), dir(d2))
#
# d3 = {1:'Sreeni', 2:'Pavan', 3:'Ramya', 4:'Chaturya',1:'Kunal'}
#
# # syntax : {key:value, key2:value, key3: value}
#
# print("d3 details", d3, type(d3),id(d3), dir(d3))
#
# d3.update({5:'Rahul'})
# print("d3 details after update", d3, type(d3),id(d3), dir(d3))
#
# d3.update({ 1:'Sreenivas', 6:'Pritam'})
#
# print("d3 details after update 1 name tp Sreenivas", d3, type(d3),id(d3), dir(d3))
#
# d3.setdefault(8)
#
# print('d3 before pop', d3)
# # d3.pop(8)
# # d3.pop(1)
# d3.popitem()
# d3.popitem()
# d3.popitem()
# d3.popitem()
# print("d3 after popitem", d3)
#
#
# d3.pop(1)
#
# print("d3 after popitem", d3)
#
# print("fetching values using key", d3.get(10))
#
# # print("fetching values using indexed based syntax", d3[10]) # 2 is key
#
# print("keys", d3.keys(), type(d3.keys()))
#
# print("values", d3.values(), type(d3.values()))
#
# print("key and value", d3.items(), type(d3.items()))


a=1

ls=[1,2,3]

print(id(a))

print(id(ls), id(ls[0]))