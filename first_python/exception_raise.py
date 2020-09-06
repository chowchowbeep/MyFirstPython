def userid(lang):
    if lang == 'python':
        raise Exception("파이썬!!") # 임의로 exception을 발생시킴
    print(lang)


if __name__ == "__main__":
    try:
        userid("java")
        userid("python")
    except Exception as e: # Exception타입의 예외객체를 변수e로 사용
        print(e.args[0]) #