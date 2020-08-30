# 빈 리스트 객체 생성
list_rec = list([])
list_rec.append(input("학번 입력=>"))
list_rec.append(input("이름 입력=>"))
list_rec.append(int(input("국어 입력=>")))
list_rec.append(int(input("영어 입력=>")))
list_rec.append(int(input("수학 입력=>")))


list_rec.append(list_rec[2] + list_rec[3] + list_rec[4])
list_rec.append(list_rec[5] / 3)

print("\n학번 이름 국어 영어 수학 총점 평균")
print("============================")
print("%4s %3s %3d %3d %3d %3d %6.2f" %
      (list_rec[0], list_rec[1], list_rec[2], list_rec[3],
       list_rec[4], list_rec[5], list_rec[6]) )
print(list_rec)
len(list_rec)

