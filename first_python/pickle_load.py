import pickle


# pickcle_dump.py에서 직렬화하여 저장된 파일을 역직렬화하여 출력

# 역직렬화를 가능하게 하는 pickle모듈의 load메소드
if __name__ == "__main__":
    fp = open("binary.dat", "rb") # binary.dat파일을 binary형태로 read함
    data = pickle.load(fp)
    print(data)
    data = pickle.load(fp)
    print(data)
    data = pickle.load(fp)
    print(data)
    data = pickle.load(fp)
    print(data)
    data = pickle.load(fp)
    print(data)
    data = pickle.load(fp)
    print(data)
    data = pickle.load(fp)
    print(data)
    fp.close()
