# def calc(a,b):
#     return a+b
#
# print(calc(4,5))
#
# def calc(a,b,c):
#     return a+b+c
#
# print(calc(4,5,10))
# def calc(a,b,c,d):
#     return a+b+c+d
# print(calc(7,8,9,10))
# print(calc(4,5))


def calc(a,b,*args):
    print("args is ", args, type(args),a,b)
    total = 0
    for i in args:
        total += i

    return total

calc(1,2,3,4,5)

# print("sum of calc(1) : ", calc(1))
# print("sum of 1 & 2 : ", calc(1,2))
# print("sum of 1,2 & 10 :", calc(1,2,10))
# print("sum of all:", calc(1,2,10,7,6,6,64,5,5,6,7,8,9,110,10))
# calc(90,100)


def calc(a,b,**kwargs):
    print("kwargs is ", kwargs,type(kwargs), a,b)
    total = 0
    for i in kwargs.values():
        total += i

    return total

calc(1,b=2,c=3,d=4,e=5)

# print(calc(a=1,b=2))
# print(calc(a=1,b=2,c=50))
# calc(e=0,k=90, l='etl')



