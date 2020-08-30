# 빈 dict 객체 생성
dict_rec = {}
dict_rec["hakbun"] = input("학번 입력=>")
dict_rec["name"] = input("이름 입력=>")
dict_rec["kor"] = int(input("국어 입력=>"))
dict_rec["eng"] = int(input("영어 입력=>"))
dict_rec["math"] = int(input("수학 입력=>"))


dict_rec["tot"] = dict_rec["kor"] + dict_rec["eng"] + dict_rec["math"]
dict_rec["avg"] = dict_rec["tot"]/3

print("\n학번 이름 국어 영어 수학 총점 평균")
print("============================")
print("%4s %3s %3d %3d %3d %3d %6.2f" %
      (dict_rec["hakbun"], dict_rec["name"], dict_rec["kor"], dict_rec["eng"],
       dict_rec["math"], dict_rec["tot"], dict_rec["avg"]) )
print(dict_rec)






