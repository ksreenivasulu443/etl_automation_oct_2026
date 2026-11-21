#
# def calc(a,b):
#     print("a value is", a)
#     print("b value is", b)
#     print("sum of a & b is", a+b)
#     print("multiplication is", a*b)
#     print("division is", a/b)
#     print("remainder is", a%b)
#     print("floor division is", a//b)
#     return a+b, a-b, a*b, a/b, a//b, a%b, a**b
#
# calc(a=1,b=2)
#
# def calc(a,b,c):
#     return a+b+c
#
# print(calc(a=5,b=7,c=10))

def count_validation(source_count, target_count):
    if source_count > target_count:
        print("Source count is greater than target count")
        str1 = "Source count is greater than target count"
        status ='FAIL'
    elif source_count < target_count:
        #print("Source count is less than target count")
        status ='FAIL'
        str1 = "Source count is less than target count"
    else:
        print("Source count is equal to target count")
        str1 = "Source count is equal to target count"
        status ='PASS'

    return  str1
    return "Hello"

print(count_validation(source_count=1, target_count=1))


# sum of n number
# sum of even or odd
# palindrome

def sum_of_n_number(num):
    total = 0
    for n in range(1,num+1):
        total += n
    return total

print(sum_of_n_number(10))


