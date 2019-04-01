# 函数


def function1():
    print('invoke function')
    print('hello world')


function1()


print('-----------')


def function2(name):
    print('参数是: ' + name)


function2('china')

print('---------')


def function3(a, b):
    return a + b


print(function3(4, 5))


print('----------')


def function4(a = '0', b = '8'):
    print('a = ' + a + ', b = ' + b)


function4(b = '5', a = '3')


print('---------')


def function5(*params):
    print(len(params))


function5(1, 2, 3, 4, 5)


print('-----------')


def function6(name):
    temp = name + 'aaaaa'
    print(temp)


function6('123')


print('----------')

def function7(name):
    global temp
    temp = name + 'aaaa'
    print(temp)


function7('55555')
print(temp)

print('---------')


def function8():
    print('888888888')
    def fun():
        print('0000000')
    fun()


function8()

print('----------')





