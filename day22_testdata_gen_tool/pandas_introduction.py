import pandas as pd
from pandasql import sqldf
import numpy as np

# df = pd.DataFrame()
#
# print("df details", df, type(df), dir(df))
#
# dict_data = {'id':[1,2,3,4], 'name':['Sreeni','Rahul','Ramya','Rudrani']}
#
# print("data details", dict_data, type(dict_data), dir(dict_data))
#
# df_with_dict = pd.DataFrame(data=dict_data)
# print("==="*40)
# print("df_with_dict")
# print(df_with_dict)
# print("==="*40)
# print("disply only sreeni row")
# print(sqldf("select id, upper(name) as name from df_with_dict where name = 'Sreeni' "))
# print("==="*40)

# print("2. DATAFRAME FROM LIST OF TUPLES")
# print("=" * 60)

# d = [
#     (101, "John"),
#     (102, "David"),
#     (103, "Smith")
# ]
#
# df = pd.DataFrame(
#
#    columns =["customer_id","name"],
#     data=d,
# )
#
# print(df)



#
# print("6. DATAFRAME FROM NUMPY ARRAY")
# print("=" * 60)
#
# d = np.array([
#     [101, 25],
#     [102, 30],
#     [103, 35]
# ])
#
# df = pd.DataFrame(
#     data=d,
#     columns=["customer_id", "age"]
# )

# print(df)

df_csv = pd.read_csv(filepath_or_buffer=r"C:\Users\Haritha\PycharmProjects\etl_automation_oct_2026\day22_testdata_gen_tool\customer_with_header.csv")
print(df_csv)



df = sqldf("select customerid, customername, email from df_csv where city = 'Bangalore' ")

df.to_csv('customer_filter_row.csv')


