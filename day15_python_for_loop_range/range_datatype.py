

# range(stop=10) # 0,9
# range(start=1, stop=10) # 1, 9
# range(start=1, stop=10, step=1) # 1 to 9

# r = range(10)
# print("r details", r, type(r), r.__sizeof__() , dir(r))
#
# for i in range(10):
#     print(i)


# for i in range(1,1001):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# generate numbers from 1-10 and print sum of n number

# for i in range(1,11):
#     print(i)

# sum of n numbers


for i in range(1,11):
    total = 0
    total = total + i

print("total", total)

# n(n+1)/2
#
# 10(10+1)/2

# even & odd sum

even_sum = 0
odd_sum = 0

for i in range(1,6):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print("even_sum", even_sum)
# print("odd_sum", odd_sum)
# print("total", even_sum+odd_sum)

# for i in range(-10, -20, -2):
#     print(i)

# table = 4
# for num in range(1,11):
#     print(f"{table}x{num} = {table*num} ")

for i in range(1,100): # start = 0 and stop=4
    for j in range(1,11): # start =0 and stop =2
        print(f"{i}x{j} = {i*j}" )


for i in range(1, 5, 2):
    print(i)

