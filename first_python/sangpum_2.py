# -*- coding: utf-8 -*-
class Sangpum:
    def __init__(self):
        self._code = ""
        self._irum = ""
        self._su = 0
        self._price = 0
        self._kumack = 0
    def input_sangpum(self):
        self._code = input("제품코드 입력 => ")
        if (obj._code == "exit"):
            return True
        self._irum  = input("제품명 입력 => ")
        self._su = int(input("수량 입력 => "))
        self._price = int(input("단가 입력 => "))
        return False

    def process_sangpum(self):
        self._kumack = self._su * self._price

    def output_sangpum(self):
        print("%4s      %4s     %4d     %6d     %8d" %
              self._code, self._irum, self._su, self._price, self._kumack)


if __name__ == "__main__":

    lst = []

    while True:
        obj = Sangpum()
        if obj.input_sangpum():
            break
        obj.process_sangpum()
        lst.append(obj)
        print()

    print("\n                   *** 상품정보 ***")
    print("======================================================")
    print("제품코드      제품명        수량          단가       판매금액")
    print("=================ㅇ=====================================")
    for data in lst:
        data.output_sangpum()
    print("======================================================")