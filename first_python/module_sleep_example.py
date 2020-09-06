import time


if __name__ == "__main__":
    #input("Enter a number:")
    t1 = time.time() # 코드수행 전 시각
    #time.sleep(3)

    for i in range(10000):
        for j in range(1000):
            pass

    #input("Enter a number again:")
    t2 = time.time() # 코드수행 후 시각

    time_gap = t2 - t1 # 특정 코드를 실행하는데 걸리는 시간을 대략적으로 계산해볼 수 있음

    print("Time gap:", time_gap)