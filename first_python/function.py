'''
def add(a,*b,c):
    hap = a
    hap += c
    print("튜플 b",b)
    print("인자 c")
    for val in b:
        hap += val
    return hap

print(add(10,20,c=30))
print(add(10,20,30,c=40))
'''
'''
def add(a,**b,*d): # 일반, 가변, 정의되지 않은 매개변수
    hap = ad
    print("dict b",b)
    print("tuple d", d)
    for val in b:
        print(val)
        hap += b[val]
    return hap

print(add(10,20,30,aa=20,bb=30,c=40))
#print(add(10,aa=20,bb=30,cc=40))
'''


def inputNum():
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    return num1, num2

def compareNum(num1, num2):
    if num1 > num2:
        min_num = num2
        max_num = num1
    else:
        min_num = num1
        max_num = num2
    return min_num, max_num

def cntPrime(min_num, max_num):
    cnt = 0
    for i in range(min_num, max_num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else: # 소수인 경우 수행
            print("%5d " % (i), end="")
            cnt += 1 # 소수의 갯수 카운트
            if cnt % 10 == 0: # 소수의 갯수가 10의 배수이면 줄바꿈 수행
                print()
    return cnt

def showPrime(cnt):
    if cnt % 10 != 0:
        print()
    print("총소수의 갯수 = %d" % (cnt))


 # 모듈 생성시 추가. 외부에서 불필요한 문장이 실행되지 않도록 함.
if __name__ == "__main__":
    num1, num2 = inputNum()
    min, max = compareNum(num1,num2)
    cnt = cntPrime(min,max)
    showPrime(cnt)