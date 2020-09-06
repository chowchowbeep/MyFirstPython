'''
fp = open("text.txt", "rt", encoding="utf-8")
lines = fp.readlines() # 개행문자를 기준으로 리스트 형식으로 반환
#print(lines)
for line in lines:
    print(line, end="") # 문장마지막의 줄바꿈문자를 없애고 출력
fp.close()
'''

# with구문을 사용하면 close()메소드 없이 파일 자동 종료
with open("text.txt", "rt", encoding="utf-8") as fp:
    lines = fp.readlines() # 개행문자를 기준으로 리스트 형식으로 반환
    for line in lines:
        print(line.strip()) # 문장마지막의 줄바꿈문자를 없애고 출력



