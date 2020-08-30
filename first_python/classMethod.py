class CircleCalculator:
    __PI = 3.14

    @classmethod #클래스가 정의되면 객체가 생성되지 않아도 사용가능한 클래스메소드임을 명시하는 어노테이션
    def calculate_area(cls, radius): # 클래스메소드 정의시 첫번째 파라미터는 반드시 cls여야 함.
        area = cls.__PI * (radius ** 2) #
        return  round(area, 2)

    @classmethod
    def caculate_circumference(cls, radius):
        circumference = 2 * cls.__PI * radius
        return  round(circumference, 2)

if __name__ == "__main__":
    print("반지름: ", 3, "면적: ", CircleCalculator.calculate_area(3))
    print("반지름: ", 3, "둘레: ", CircleCalculator.caculate_circumference(3) )