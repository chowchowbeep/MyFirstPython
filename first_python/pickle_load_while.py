import pickle

# pickcle_dump.py에서 직렬화하여 저장된 파일을 역직렬화하여 출력


'''
역직렬화를 가능하게 하는 pickle모듈의 load메소드를 이용
-> load메소드는 읽고 있는 데이터가 파일 내 마지막 데이터인지 체크하지 못하기 때문에
    더이상 읽을 데이터가 없을 경우 오류 발생. 
    이러한 오류에 대한 익셉션 처리 필요
'''

if __name__ == "__main__":
    fp = open("binary.dat", "rb")
    
    
    try: # try 블럭 내에는 예외가 발생할 수 있는 문장이 위치
        while True:
            data = pickle.load(fp) 
            print(data)
    except: # 예외발생시 실행할(예외처리할) 문장
        print("프로그램 종료!")
        #pass
    

    fp.close()