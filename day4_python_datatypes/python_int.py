''' documentation strings - this is used to track file changes and meta data of python file
This file is created to practice python int type
created by : Sreeni
created on : 14-OCT-2026
updated by:
updated on:
comments:

Data type is a classification of data that specifies which type of value a variable can hold,
how it behaves, and what operations can be performed on it

'''


a = 10
a = 11

print("a value", a )
print("type of a", type(a))  # type is built in function which displays datatype of variable or value
print("id/memory of a ", id(a)) # id display memory location of value or variable value, this will change when you rerun the code
print("methods of a", dir(a)) # dir always display methods/functions available on specific datatype, __ double undescore methods are special methods in python
print("size of a", a.__sizeof__()) # size of value

print('='*200)

b = '10'

print("b value", b )
print("type of b", type(b))
print("id/memory of b ", id(b))
print("methods of b", dir(b))
print("size of b", b.__sizeof__())

str1 = 'ETL automation'

print("upper of str1", str1.upper())

print('='*100)

c = 0.0

print("c value", c )
print("type of c", type(c))  # type is built in function which displays datatype of variable or value
print("id/memory of c ", id(c)) # id display memory location of value or variable value, this will change when you rerun the code
print("methods of c", dir(c)) # dir always display methods/functions available on specific datatype, __ double undescore methods are special methods in python
print("size of c", c.__sizeof__()) # size of value



d = -10
print("abs", abs(d))
print("abs", d.__abs__())

a = 10

a = 20



