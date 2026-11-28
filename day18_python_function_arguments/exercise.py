def f(arg1, arg2, arg3=4, arg4=8 ): # default
    print(arg1, arg2, arg3, arg4)

# f(3,2) # 3,2 are positional 3,2,4,8
# f(10,20,30,40) #  all values in f call positional arguments
# f(25,50,arg4=100)
# f(arg4=2,arg1=3,arg2=4) # keyword arguments
# f(a=10,b=20) # f() got an unexpected keyword argument 'a'
#f() #f() missing 2 required positional arguments: 'arg1' and 'arg2'
#f(arg3=10,arg4=20,30,40) #SyntaxError: positional argument follows keyword argument
# f(4,5,arg2=6) #TypeError: f() got multiple values for argument 'arg2'
# f(4,5,arg3=5,arg5=6) # TypeError: f() got an unexpected keyword argument 'arg5'
f(4,5,5,arg3=2) # f() got multiple values for argument 'arg3'

def f2(arg1, arg2, arg3=4, arg4=8 ): # default
    print(arg1, arg2, arg3, arg4)
