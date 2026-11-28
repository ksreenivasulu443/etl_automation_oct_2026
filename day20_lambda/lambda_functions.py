#doc strings

#syntax lambda

# lambda par1,par2,par3:expression

# calc_lambda = lambda a,b,c : a+b+c


# def calc_traditional(a,b,c):
#     return a+b+c, a*b*c
#
# print("lambda o/p", calc_lambda(1,2,3))
#
# print('traditional function o/p', calc_traditional(1,2,3))


col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']


# def cleansing_column_names(columns):
#     formatted_columns = []
#     for col in columns:
#         formatted_columns.append(col.strip().lower().replace(' ', '_'))
#
#     return formatted_columns
#
# print(cleansing_column_names(columns=col_names))

#
# col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']
# cleansing_column_names_lambda = lambda column: column.strip().lower().replace(' ', '_')
# print('lambda with map' , list(map(cleansing_column_names_lambda,col_names )))


# filter, sorted, reduce

## I want to bulit function to filter columns which name keyword at the end

# col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']
# column_ending_with_name = lambda column : column.endswith('name')
#
# print("column ending name", list(filter(column_ending_with_name, col_names)))
#
# print(column_ending_with_name('first_name123'))
#
#
# col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']
# def display_cols_ends_with_keyword(col_names,keyword):
#     ends_with_name_cols =[]
#     for i in col_names:
#         if i.strip().lower().endswith(keyword):
#             ends_with_name_cols.append(i.strip().lower().replace(' ',''))
#     return ends_with_name_cols

# col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']
# column_ending_with_name = lambda column : column.strip().lower().replace(' ', '_').endswith('name')
# print('column_ending_with_name', column_ending_with_name('first name'))
# print("column ending name", list(map(cleansing_column_names_lambda,
#                                      list(filter(column_ending_with_name, col_names)))))

# map(lambda, iterable) # ['first_name', 'last_name', 'age', 'full_name', 'email']
# filter(lambda, iterable) # [' First_name ', 'Last_Name  ', 'Full name   ']

# col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']
# def display_cols_ends_with_keyword(col_names,keyword):
#     ends_with_name_cols =[]
#     for i in col_names:
#         if i.strip().lower().endswith(keyword):
#             ends_with_name_cols.append(i.strip().lower().replace(' ',''))
#     return ends_with_name_cols


# print(list(filter(lambda num : num % 2 == 0, range(11))))
#
# print(list(map(lambda num : num ** 2, range(10))))



# print(list(filter(calc, range(10))))

from functools import reduce
calc = lambda a,b : a+b


total = reduce(calc, [1,2,3,4,5])  #[15]
print(total)


# write sum of n numbers using lambda


# def even_odd(num):
#     ls = []
#     for i in range(10):
#         if i % 2 == 0:
#             print(i)
#             ls.append(i)


names = ["Python", "SQL", "Automation", "ETL"]

# names.sort(reverse=True)

# print(names)

names.sort(key=lambda x: len(x), reverse=True)
#
print(names)














