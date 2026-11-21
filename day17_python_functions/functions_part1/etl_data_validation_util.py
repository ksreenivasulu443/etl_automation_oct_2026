#syntax

# def function_name(par1,par2, par3.....parn):
#     #code
#     #return

def greeting():
    print("Welcome to the ETL Automation Labs")

# greeting()
def greeting_with_name(name): # name is parameter
    print(f"Hello {name} welcome to the ETL Automation Labs")

# greeting_with_name( name = 'Sreeni') # name is argument, keyword argument
#
# # greeting_with_name('Sreeni') # positional argument
#
# greeting()


def calc(a,b):
    print("a value is", a)
    print("b value is", b)
    print("sum of a & b is", a+b)
    print("multiplication is", a*b)
    print("division is", a/b)
    print("remainder is", a%b)
    print("floor division is", a//b)
    return a+b, a-b, a*b, a/b, a//b, a%b, a**b

out = calc(a=5,b=7) # this print prints function return

# print("sum", out[0]) # if we call function with two or more returns output type will be tuple
# print("sub", out[1])
# print("mul", out[2])

# out = calc(a=5,b=7)



def calc(a,b,c):
    return a+b+c

calc(a=5,b=7)
