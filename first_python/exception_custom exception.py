
# Exception class를 상속받아 사용자 정의 Exception class를 만듦
class JumsuException(Exception):
    def __init__(self, msg):
        self._message = msg

def input_jumsu():
    jumsu = int(input("점수 입력 => "))
    if jumsu < 0:
        raise JumsuException("0이상만 가능")
    elif jumsu > 100:
        raise JumsuException("100이하만 가능")
    else:
        return jumsu


if __name__ == "__main__":
    try:
        jumsu = input_jumsu()
    except JumsuException as e:
        print(e.args[0])
    else:
        print("점수는 %d점입니다." % jumsu)