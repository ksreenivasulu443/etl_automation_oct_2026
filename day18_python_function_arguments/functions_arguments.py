
def calc(a,b):
    print("a value is ", a)
    print("b value is ", b)
    return a+b, a/b, a%b

# print(calc(3,4)) # 3,4 are positional arguments

# print(calc(5,6,4))




# print(calc(a=10,b=20)) # a=10 and b=20 are keyword arguments

# print(calc(b=10))
# print(calc(5))
# print(calc(b=200,c=500))

# print(calc(b=200.5,a=-500.0))

# print(calc(a='sreeni',b='kattu'))




# def calc(a,b,c,d):
#     print("a value is ", a)
#     print("b value is ", b)
#     print("c value is ", c)
#     print("d value is ", d)
#     return a+b+c+d

# print(calc(1,2,3,4))
# print(calc(c=7,d=8,a=5,b=6))

# print(calc(1,2,c=3,d=4)) # 1,2 are positional and c=3, d=4 are keyword arguments

# print(calc(a=1,b=2,3,4))
# print(calc(1,2,3,a=5))
# print(calc(1,2,d=3,c=4))
#SyntaxError: positional argument follows keyword argument
# if we want to call function with keyword and positional arguments
#     1. provide all positional first and then keyword


def calc(a,b,c,d, e=50): # e is default parameter
    print("a value is ", a)
    print("b value is ", b)
    print("c value is ", c)
    print("d value is ", d)
    print("e value is ", e)
    return a*b*c*d*e

# print(calc(1,2,3,4))

print(calc(1,2,3,4,5))

print(calc(a=1,b=2,c=3,d=4,e=5))

print(calc(e=50,a=10,b=20,c=30,d=40))