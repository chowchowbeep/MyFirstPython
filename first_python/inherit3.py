class A:
    def __init__(self, x):
        self.aa = x

    def printA(self):
        print(self.aa)


class B(A):
    def __init__(self, x, y):
        super().__init__(x) #A.__init__(self, x)    #super(B, self).__init__(x)와 동일
        self.bb = y

    def printB(self):
        print(self.bb)


class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y) #B.__init__(self, x, y)    #super(C, self).__init__(x, y)
        self.cc = z

    def printC(self):
        print(self.cc)


if __name__ == "__main__":
    obj = C(100, 200, 300)
    print(obj.cc)
    print(obj.bb)
    print(obj.aa)
    print()
    obj.printA()
    obj.printB()
    obj.printC()