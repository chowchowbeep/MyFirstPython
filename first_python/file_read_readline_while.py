fp = open("text.txt", "rt", encoding="utf-8")


while True:
    line = fp.readline() # 더이상 남아 있는 행이 없을 경우 ""반환
    if line == "": # 더이상 출력할 것이 없으면 while문 종료
        break
    print(line.strip()) # 또는 print(line, end='') # 마지막문자열 \n개행문자를 없애고 출력

fp.close()