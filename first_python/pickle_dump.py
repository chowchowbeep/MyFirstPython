import pickle # 직렬화 / 역직렬화를 가능하게 하는 모듈

'''
    [ 직렬화 / 역직렬화 ]
    - 직렬화 : 
        구조화된 형태를 연속된 문자열로 변환.
    - 역직렬화 : 
        직렬화된 것을 다시 구조화된 형태로 변환.
    - 직렬화 / 역직렬화의 사용
        객체 -> 파일로 출력위해 직렬화
        파일 -> 객체로 변환위해 역직렬화
'''

# 직렬화를 가능하게 하는 pickle모듈의 dump메소드
if __name__ == "__main__":
    fp = open("binary.dat", "wb") # binary.dat파일을 binary형태로 write함
    pickle.dump(1, fp)
    pickle.dump(3.14, fp)
    pickle.dump("Hello World", fp)
    pickle.dump("안녕 파이썬!", fp)
    pickle.dump([1, 2, 3], fp)
    pickle.dump((1, 2, 3), fp)
    pickle.dump({"line":0, "rectangle":1, "triangle":2}, fp)
    fp.close()



