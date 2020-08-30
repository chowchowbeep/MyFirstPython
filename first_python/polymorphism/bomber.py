from airforce import AirForce

# AirForce로부터 오버라이딩
# 오버라이딩(Overriding) : 부모클래스의 메소드를 자식클래스에서 재정의하는 것

class Bomber(AirForce):
    def __init__(self, bomb_num):
        self._bomb_num = bomb_num

    def take_off(self):
        print("폭격기 발진")

    def fly(self):
        print("폭격기 목적지로 출격")

    def attack(self):
        for i in range(self._bomb_num):
            print("폭탄 투하")
            self._bomb_num = self._bomb_num -1

    def land(self):
        print("폭격기 착륙")