#自定义属性


class Temp:

    s = ''

    def getProperty(self):
        return self.s

    def setProperty(self, s):
        self.s = s

    def delProperty(self):
        del self.s

    x = property(getProperty, setProperty, delProperty)



t = Temp

t.x = '1111'

print(t.x)


