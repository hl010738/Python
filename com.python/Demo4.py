# 数组

member = ['aaa', 'bbb']
print(member)

print('----------')

member.append('ccc')
print(member)

print('--------')

member = ['aaa', 123, ['111', '2222']]
print(member)

print('--------')

extend = ['6666', '7777']
member.extend(extend)
print(member)

print('---------')

member.insert(2, [1 == 1, 2 == 3])
print(member)

print('--------')

print(member[1])

print('-------')

member.remove('aaa')
print(member)

print('-------')

del member[4]
print(member)

print('---------')

pop = member.pop()
print(pop)

print('---------')


