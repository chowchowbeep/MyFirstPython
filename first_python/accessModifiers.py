class Circle:
    PI = 3.14 # 클래스변수  클래스내, 메소드 밖에 선언된 변수 java의 static과 비슷 객체 생성이 몇 개가 되든 하나만 존재함

    def __init__(self, radius):
        self._radius = radius


    def get_radius(self):
        return self._radius

    def get_area(self):
        area = Circle.PI * (self._radius **2)
        return round(area, 2)

    def get_circumference(self):
        circumference = 2 * Circle.PI * self._radius
        return round(circumference, 2)

if __name__ == "__main__":
    circle1 = Circle(3)
    print("원주율: ", Circle.PI)   # 클래스 변수값은 클래스명.클래스변수명으로 접근가능
    print("반지름: ", circle1.get_radius(), "면적: ", circle1.get_area())
    print("반지름: ", circle1.get_radius(), "둘레: ", circle1.get_circumference())

    circle2 = Circle(4)
    print("반지름: ", circle2.get_radius(), "면적: ", circle2.get_area())
    print("반지름: ", circle2.get_radius(), "둘레: ", circle2.get_circumference())