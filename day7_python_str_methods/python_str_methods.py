str1 = ' ETL automation labs '

print("strip", str1.strip(), len(str1), len(str1.strip()))
print("lstrip", str1.lstrip(), len(str1), len(str1.lstrip()))
print("rstrip", str1.rstrip(), len(str1), len(str1.rstrip()))


str2 = '423  ETL 123121   45 '
print("strip with words", str2.strip('45 ') )

# 423  ETL 123121

str3 = '#$@!ETL @###%^'
print(str3.strip('$#@%^'))
#
# $@!ETL @###%^
#
# @!ETL @###%^
#
# !ETL @###%^
#
# !ETL

str2 = '423  ETL 12453121   45 '
print("strip with words", str2.strip('45 ') )

# 23  ETL 123121

str4 = 'ETL Auto'
print(str4.strip('TEto'))

str4 = 'Welcome to ETL Automation labs'

print("SPLIT", str4.split(), type(str4.split()))

not_null_cols = "col1,col2,col3,col4"

print("split not null cols", not_null_cols.split(sep=','))

path = "C:\\Users\\Haritha\\PycharmProjects\\etl_automation_oct_2026\\day7_python_str_methods\\python_str_methods.py"
path2 = r"C:\Users\Haritha\PycharmProjects\etl_automation_oct_2026\day7_python_str_methods\python_str_methods.py"


print(path2)


print("split path", path2.split('\\')[-1])

not_null_cols = "col1,col2,col3,col4"

print("split not null cols", not_null_cols.split(sep=',', maxsplit=2))

print("rsplit not null cols", not_null_cols.rsplit(',', 2))

ls = ['1','2','3','4','5']

print("join", ",".join(ls), type(",".join(ls)))

cols = ['col1','col2','col3']

sql_query = f"select {','.join(cols)} from table"

print("sql_query", sql_query)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 50))

val = 40

print(f"The price of apple is {val}")


name = 'Hari'
age = 25

print("person name", name, "and age is", age)

print(f"person name {name} and age is {age} ")

print("person name {name} and age is {age} ".format(name=name, age=age))







