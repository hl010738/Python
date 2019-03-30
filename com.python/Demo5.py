
#字符串

str = '123456789'

str1 = str[:4]

str2 = str[4:]

str3 = '插入的字符串'

print(str1 + str3 + str2)

print('-------------')

str = 'skjvnljafsfe'
str = str.capitalize()
print(str)

print('------------')

string = '111122222'
string = string.translate(str.maketrans('1', '3'))
print(string)
