# A <- C -> B 상속구조

class A:
    def __init__(self):
        self.aa = 10

    def printData(self):
        print("Class A")

    def printA(self):
        print("printA() 실행")


class B:
    def __init__(self):
        super().__init__()
        self.bb = 20

    def printData(self):
        print("Class B")

    def printB(self):
        print("printB() 실행")


# 다중상속 (다수의 부모클래스를 상속)
# 파이썬에서는 부모클래스가 다수일 때, 순서가 중요함
# class C(B,A): 라면, 먼저 등장한 B클래스만 super().__init__() 에서 생성됨
class C(A, B):
    def __init__(self):
        super().__init__() # A클래스만 생성자로 생성됨
        self.cc = 30

    def printC(self):
        print(self.cc)


if __name__ == "__main__":
    obj = C()
    print(obj.cc)
    # print(obj.bb) #B클래스는 c클래스에서 생성자로 생성되지 않았기 때문에 B클래스의 속성은 접근불가
    print(obj.aa)
    print()
    obj.printA()
    obj.printB() #B클래스가 생성자로 생성되지 않아도 B클래스의 메소드는 사용가능
    obj.printC()
    obj.printData() # B클래스의 printData()메소드는 상속되지 않음.
    # 다수의 부모상속자가 동명의 메소드를 갖고 있다면, 먼저 파라미터로 들어온 클래스의 메소드만을 상속


'''
C클래스의 객체에는 
aa = 10
bb = 20 -> 접근불가
cc = 30 

A클래스의 printData()
A클래스의 printA()
B클래스의 printB()
C클래스의 printC()

들이 클래스멤버로 저장
'''
