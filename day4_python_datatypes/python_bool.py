''' documentation strings - this is used to track file changes and meta data of python file
This file is created to practice python bool type
created by : Sreeni
created on : 14-OCT-2026
updated by:
updated on:
comments:

Data type is a classification of data that specifies which type of value a variable can hold,
how it behaves, and what operations can be performed on it

'''


# a = True
#
# print("a value", a )
# print("type of a", type(a))  # type is built in function which displays datatype of variable or value
# print("id/memory of a ", id(a)) # id display memory location of value or variable value, this will change when you rerun the code
# print("methods of a", dir(a)) # dir always display methods/functions available on specific datatype, __ double undescore methods are special methods in python
# print("size of a", a.__sizeof__()) # size of value
#
# print('='*100)
#
# b = True
#
# print("b value", b )
# print("type of b", type(b))
# print("id/memory of b ", id(b))
# print("methods of b", dir(b))
# print("size of b", b.__sizeof__())

with open("logfile_ddmmyyyhhmiss.log", "a") as f:
    print("Welcome to ETL Automation Labs", file=f, end='\t')
    print("Learning Python Programming", file=f, end='\n')
    print(100, 200, 300,sep='|', file=f)

# import time
#
#
# for i in range(1, 6):
#     print(i, flush=True)
#     time.sleep(2)



