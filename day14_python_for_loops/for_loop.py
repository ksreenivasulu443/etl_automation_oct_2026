#syntax

# for item in collect_of_item(list,tuple, set, frozenset, dict, range, string):
#     statements



# ls = [1,2,3,4,5]
#
# for num in ls:
#     print("num is", num)
#
# print("this is outside loop")


# t = (8,'test',11, 'etl', 11)
# for num in t:
#     if isinstance(num,int):
#         if num % 2 == 0:
#             print(f"{num} is even")
#         else:
#             print(f"{num} is odd")
#     else:
#         print(f"{num} is not integer")

s = {1,1,1,1,2,2,2}

# print("s is", s)
#
# for i in s:
#     print(i)


# fs = frozenset({1,1,1,1,2,2,2})
#
# print("fs is", fs)
#
# for i in fs:
#     print(i)


str1 = 'Etl 123 a'
vowels = 'aeiou'# ['a','e','i','o','u'] or ('a','e','i','o','u')

for char in str1:
    if char.isalpha():
        if  char.lower() in vowels  : #t in (aeiou)
            print(f"{char} is vowel")
        else:
            print(f"{char} is consonant")
    else:
        print(f"{char} is not a alphabetic character")
