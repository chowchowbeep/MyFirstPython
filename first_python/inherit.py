# A <- B <- C 상속구조

class A(): # class A(object)의 object가 생략된 형태 -> 모든 클래스는 object를 상속함
    def __init__(self):
        self.aa = 10

    def printA(self): # def __printA(self): 에서처럼 접근제한자가 있는 속성, 메소드는 상속 불가
        print(self.aa)

class B(A): # A : 부모클래스, 슈퍼클래스, 상위클래스   # B: 자식클래스, 파생클래스, 하위클래스
    def __init__(self):
        super().__init__() #A.__init__(self)    #super(B, self).__init__()  와 동일 (부모클래스와 자신클래스 생성)
        self.bb = 20 #B클래스에서 사용할 속성이 '추가'됨(상위클래스의 속성도 사용할 수 있는 상태임)

    def printB(self): 
        print(self.bb)
    # 부모클래스의 메소드는 부모클래스의 생성자없이도 사용가능, but 부모클래스의 속성은 부모클래스의 생성자없이 사용불가

class C(B): # 단일상속 (부모클래스를 하나만 상속)
    def __init__(self):
        super().__init__() #B.__init__(self)    #super(C, self).__init__()  와 동일
        self.cc = 30

    def printC(self):
        print(self.cc)

# C객체에는 A,B객체의 속성과 메소드가 모두 저장되어 있음


if __name__ == "__main__":
    obj = C()
    print(obj.cc)
    print(obj.bb)
    print(obj.aa)
    print()
    obj.printA()
    obj.printB()
    obj.printC()

