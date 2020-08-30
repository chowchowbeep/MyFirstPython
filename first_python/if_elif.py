# 빈 dict 객체 생성
'''
dict_rec = {}
dict_rec["hakbun"] = input("학번 입력=>")
dict_rec["name"] = input("이름 입력=>")
dict_rec["kor"] = int(input("국어 입력=>"))
dict_rec["eng"] = int(input("영어 입력=>"))
dict_rec["math"] = int(input("수학 입력=>"))


dict_rec["tot"] = dict_rec["kor"] + dict_rec["eng"] + dict_rec["math"]
dict_rec["avg"] = dict_rec["tot"]/3


if dict_rec["avg"] >= 90:
    dict_rec["grade"] = "수"
elif dict_rec["avg"] >= 70:
    dict_rec["grade"] = "우"
elif dict_rec["avg"] >= 50:
    dict_rec["grade"] = "미"
elif dict_rec["avg"] >= 30:
    dict_rec["grade"] = "양"
else:
    dict_rec["grade"] = "가"


print("\n학번 이름 국어 영어 수학 총점 평균 등급")
print("============================")
print("%4s %3s %3d %3d %3d %3d %6.2f %2s" %
      (dict_rec["hakbun"], dict_rec["name"], dict_rec["kor"], dict_rec["eng"],
       dict_rec["math"], dict_rec["tot"], dict_rec["avg"], dict_rec["grade"]) )
print(dict_rec)

'''


# list
# 빈 리스트 객체 생성
list_rec = list([])
list_rec.append(input("학번 입력=>"))
list_rec.append(input("이름 입력=>"))

list_rec.append(int(input("국어 입력=>")))
list_rec.append(int(input("영어 입력=>")))
list_rec.append(int(input("수학 입력=>")))


list_rec.append(list_rec[2] + list_rec[3] + list_rec[4])
list_rec.append(list_rec[5] / 3)
print(list_rec[6])


if list_rec[6] >= 90:
    list_rec.append("수")
elif list_rec[6] >= 70:
    list_rec.append("우")
elif list_rec[6] >= 50:
    list_rec.append("미")
elif list_rec[6] >= 30:
    list_rec.append("양")
else:
    list_rec.append("가")


print("\n학번 이름 국어 영어 수학 총점 평균 등급")
print("==============================")
print("%4s %3s %3d %3d %3d %3d %6.2f %3s" %
      (list_rec[0], list_rec[1], list_rec[2], list_rec[3],
       list_rec[4], list_rec[5], list_rec[6], list_rec[7] ) )

print(list_rec)