#对象


class People:
    name = 'china'
    age = 10

    #构造方法 只能有一个
    def __init__(self):
        print('init...')

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name



p = People()

p.getAge()

p.setName('Japan')

p.getName()



