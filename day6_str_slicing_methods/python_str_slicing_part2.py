# # str1 = 'ETL AUTOMATION'
# #
# # print("str1[10:1]", str1[10:1], type(str1[10:1]), len(str1[10:1]))
# #
# # print("str1[10:1:-1]", str1[10:1:-1])
# #
# # print("str1[4:20]", str1[4:20])
# #
# # #print("str1[14]", str1[14]) # indexing gives error when index value in not present in the string
# #
# # # print("str1[14:]", str1[14:])
# #
# # print("str1[4:-4:1]", str1[4:-4:1])
# #
# # print("str1[4:-4:1]", str1[4:-12:1])
# #
# # dob = '16-05-2000' #dd-mm-yyyy
# #
# # # write slicing to extract mm, dd yyyy
# #
# # email = 'kats.123r@gmail.com'
#
# # username : before @
# # provider : after @ and before .
# # domain : from reverse after first .
#
# # print('MM',dob[0:2])
# # print('DD',dob[3:5])
# # print('YYYY',dob[6:10])
# # print(dob[0:2],dob[3:5],dob[6:])
# # print('YYYY',dob[-4:])
#
# # print(email[0:7],email[9:])
#
# #
# email = 'katsreen100@gmail.com'
#
# print("username", email[0:email.find('@')])
#
# print("provider", email[email.find('@'):email.rfind('.')])
# print("provider", email[email.rfind('.')])
#
# print("domain", email[-3:])
# print("domain", email[16:])
#
# str2 = 'ETL Automation Labs'
#
# print("str2.find('E')", str2.find('E'))
#
# print("str2.find('A')", str2.find('A'))
#
# print("str2.find('A')", str2.find('A'))
#
# print("str2.find('a')", str2.find('a')) # this is string method
#
# # len(str1) # builtin funct len(variable)
# #
# # print(str1) # built
# #
# # dir()
# # id()
# # type()
#
#
# str2 = 'ETL Automation Labs'
# # print("str2.find('a')", str2.find('a', 10,22))
# #
# # print("str2.find('L')", str2.find('Labs')) # Find always returns some output
# #
#
# # print("str2.find('a')", str2.find('la'))
# # # print("str2.rfind('a')", str2.rfind('a'))
# # print("str2.index('a')", str2.index('la'))
#
# # print("count/occurances a/A", str2.upper().count('A'))
# #
# # print("count/occurances A", str2.count('A'))
# #
# # print("count/occurances a", str2.count('a'))
#
#
# str2 = 'Etl auTomation Labs'
# print("lowe case", str2.lower())
# print("casefold", str2.casefold())
# print("upper case", str2.upper())
# print("capitalize", str2.capitalize())
# print("title", str2.title())
# print("swapcase", str2.swapcase())
#
#
# a = "Straße"
#
# print("a.lower()", a.lower())
# print("a.casefold()", a.casefold())
#
# hindi = "नमस्ते"
#
# print("hindi.lower()", hindi.lower())
# print("hindi.casefold()", hindi.casefold())
#
#
# str2 = 'Etl auTomation Labs'
# print("str1.endwith", str2.lower().endswith("labs")) # False
#
# print("str1.startwith", str2.upper().startswith("etl")) # False
#
# # email
#
# # gmail.com
# # .com
#
# txt = "Company12@"
#
# x = txt.isalnum()
#
# print(x)
#
#
# txt = "CompanyX"
#
# x = txt.isalpha()
#
# print(x)
#
#
# email = 'sreei@gmail.com'
#
# print("email[-3::1]:",email[-3::1])
#
#
#
# print("email[-3:-1:1]:",email[-3:-1:1])


email = 'kat@gmail.in'

atpos = email.find('@') #3

print("username", email[0:3:1])#

print("provider", email[email.find('@')+1:email.rfind('.')])
print("provider", email[email.rfind('.')+1:])



