def divide(a, b):
    try: # 예외발생가능 코드
        result = a / b
    except ZeroDivisionError: # ZeroDivisionError타입의 예외 처리코드
        print("0으로 나눌 수 없습니다.")
    except: # 예외 처리코드
        print("ZeroDivisionError 이외의 예외가 발생했습니다.")
    else: # 예외가 발생하지 않은 경우 코드
        return result
    finally: # 항상실행 
        print("나눗셈 연산입니다.")
if __name__ == "__main__":
    res = divide(5, 2); print(res, "=====") # 세미콜론;은 한 줄에 여러 명령어가 들어가는 경우
    res = divide(5, 0); print(res, "=====")
    res = divide(None, 2); print(res, "=====")