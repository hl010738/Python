
#循环

string = 'abc'
for s in string:
    print(s)

print("-------")

string2 = ['111', '222', '333']
for s in string2:
    print(s)

print("--------")

for s in range(2, 5):
    print(s)


print('----------')
for s in range(10):
    if s % 2 != 0:
        print(s)
        continue
    s += 2
    print(s)







