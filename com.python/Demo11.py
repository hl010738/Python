#继承


class Parent:
    def aaa(self):
        print('Parent')


class Par():
    def ccc(self):
        print('Par')


class Sub(Parent, Par):

    def aaa(self):
        super(Sub, self).aaa()
        print('Sub')


    def bbb(self):
        print('bbb')



s = Sub()

s.aaa()

s.bbb()





