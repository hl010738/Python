#Lambda 表达式

g = lambda x, y: x + y

print(g(4, 3))

print('-----------')


temp = range(10)
l = list(filter(lambda x: x % 2, temp))
print(l)


