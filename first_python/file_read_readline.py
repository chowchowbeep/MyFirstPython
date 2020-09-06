fp = open("text.txt", "rt", encoding="utf-8")
line = fp.readline() # readline()은 한 행씩 출력
print(line.strip()) # line이 갖고있는 \n문자 제거
line = fp.readline()
print(line.strip())
line = fp.readline()
print(line.strip())
line = fp.readline()
print(line.strip())
fp.close()
