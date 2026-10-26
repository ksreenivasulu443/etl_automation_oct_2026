

str1 = "ETL AUTOMATION"

print("str1 details", str1)
print("length of str1", len(str1))

# python index is position of char in a string/list, tuple, array, dataframes
# indexing starting zero and end at len(string)-1

#Indexing syntax
# variable[index number]

# print("First char", str1[0])
# print("Last char", str1[13], str1[len(str1)-1])
#
# print("Last char", str1[13], str1[len(str1)-1], str1[-1])
#
# print("6th index char", str1[6])
#
# print("5th index/-9th index char ", str1[-9], str1[5])

# print("str1[15]", str1[-15])

# SLICING(SUBSTRING)
# SLICING SYNTAX
# STR1[START:END:STEP]

# START : START OF STRING( INDEX AVAILABLE IN THE STRING)
# END : END OF YOUR STRING default end is last character
# STEP : HOW YOU WANT TO DISPLAY OUTPUT ALTERNATE, SEQUENCE, .... default 1








# STR1[START:END:STEP]
str1 = 'ETL AUTOMATION LABS'

print("first 3 characters", str1[0:3],len(str1[0:3]))

print("first n characters", str1[0:10:3])


print("first n characters", str1[4:14:1])

print("no end ", str1[4:])

print("no start", str1[:10])

print("no start no end", str1[:])





