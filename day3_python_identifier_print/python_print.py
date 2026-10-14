''' documentation strings - this is used to track file changes and meta data of python file
This file is created to practice python print
created by : Sreeni
created on : 12-OCT-2026
updated by:
updated on:
comments:
'''

#print is builtin function which will be used to print text messages, variables, mathematical expresion, etc

# source_name = 'customer.csv'
# target_name = 'customer_target.csv'
# source_count = 25
# print(source_name, end='-')
# print(target_name)
#
# print(source_name, target_name, source_count, sep='+')
#
# print(target_name, " ", source_count, sep='+')
#
# print("Hello world", source_name, target_name, source_count, sep='+')
#
# a = 10
# b = 20
# c = 40
#
# # print(a, b, c, sep='=')
# #
# # print(a, b, c,sep='|')
# #
# #
# print(a,b, a+b, sep='\n',end='\n')

# print(a, end='+')
# print(b, end='\n')
# print(c)
# end


# Create a file and write output
# with open("myfile.txt", "w") as my_file:
#     print("Welcome to ETL Automation Labs", file=my_file)
#     print("Learning Python Programming", file=my_file)
#     print(100, 200, 300, file=my_file)

import builtins

print(dir(builtins))

import time

with open("myfile.txt", "w") as my_file:
    for i in range(1, 6):
        print(i, file=my_file, flush=False)
        time.sleep(2)
