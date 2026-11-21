# ls1 = [1,2,3,4,5]
# ls2 = [7,8,9,10]
#
# for i in ls1: # tuple, set,fs, dict, str, range, numpy array, dataframe
#     print(i)
#     for j in ls2:
#         print(j)

d = {1:'sreeni', 2:'Ram', 3:'Sita', 4:'Nag'}

for i in d.values():
    print(i)

for i in d.keys(): # d
    print(i)


print(d.items())

for i in d.items():
    print(i, type(i), i[0], i[1])


for key, value in d.items():
    print(key, value)