
#if else

score = int(input("输入一个数字: "))
if 100 >= score >= 90:
    print('A')
elif 90 >= score >= 80:
    print('B')
else:
    print('C')

temp = '大于100' if score >= 100 else '小于100'
print(temp)
