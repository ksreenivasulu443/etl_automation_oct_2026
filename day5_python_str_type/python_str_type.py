# from multiprocessing.connection import address_type
from tkinter.font import names

#str # type cast function

str1 = 'ETL Automation'

print("str1 details", str1, type(str1), id(str1), str1.__sizeof__(), dir(str1))

str2 = "ETL Automation"

print("str2 details", str2, type(str2), id(str2), str2.__sizeof__(), dir(str2))

str3 = """ETL Automation"""

print("str3 details", str3, type(str3), id(str3), str3.__sizeof__(), dir(str3))


str4 = '''ETL Automation'''

print("str4 details", str4, type(str4), id(str4), str4.__sizeof__(), dir(str4))


str5 = """ 'It's raining outside """

print(str5)

str6 =  ''' 'It's raining outside '''

str7 = " It's raining outside "

height = "5'6"

sql = " select * from table where name= 'sreeni' "

# policy_desc
# address cols
# names
# employee
# product

primary_key = 'customer_id,customer_name'
not_null_columns = 'col1,col2,col3'


str9 = '  It"s raining outside '

str9 = '''  It"s raining outside '''

str10 = """It"s raining outside """

str11 = "  It's raining outside "

# if your string has single quote ==> 1. use double,2.use 3 double 3. use 3 single 4. escape with single

# if your string has double quote ==> 1. use single,2.use 3 double 3. use 3 single 4. escape with double


# 3 time single quotes ==> mostly used in document string
# 3 time double quotes ==>

str12 = """ ETL Testing verifies that data is correctly extracted from source systems, transformed according to "
        business rules, and loaded into the target database or data warehouse accurately. It ensures data quality, consistency, and reliability during data migration and integration."""


str13 = """address1,
         "address2 """

# description =
#
# feedback =
#
# comments =

sql_query = """ select * from source
             minus
             select * from target """

str14 = " dsahgfhudfguy43tr743537rgehwgf3r573457235^%&^%^&%&^ "