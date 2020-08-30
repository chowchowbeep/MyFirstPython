# -*- coding: utf-8 -*-

def checkScore(lst):
    while True:
        dict_rec = {}

        dict_rec["hakbun"] = input("학번 입력 => ")
        if dict_rec["hakbun"] == "exit":
            break

        dict_rec["irum"] = input("이름 입력 => ")
        dict_rec["kor"] = int(input("국어 입력 => "))
        dict_rec["eng"] = int(input("영어 입력 => "))
        dict_rec["math"] = int(input("수학 입력 => "))

        dict_rec["tot"] = dict_rec["kor"] + dict_rec["eng"] + dict_rec["math"]
        dict_rec["avg"] = dict_rec["tot"] / 3

        if dict_rec["avg"] >= 90:
            dict_rec["grade"] = "수"
        elif dict_rec["avg"] >=80:
            dict_rec["grade"] = "우"
        elif dict_rec["avg"] >=70:
            dict_rec["grade"] = "미"
        elif dict_rec["avg"] >=60:
            dict_rec["grade"] = "양"
        else:
            dict_rec["grade"] = "가"

        lst.append(dict_rec)
        print()
        return

def showScore(lst):
    print("\n               *** 성적표 ***")
    print("==============================================")
    print("학번  이름   국어  영어  수학  총점  평균  등급")
    print("==============================================")
    for data in lst:
        print("%4s %3s %4d  %4d  %4d  %4d  %5.2f  %2s"
         % (data["hakbun"], data["irum"], data["kor"], data["eng"],
            data["math"], data["tot"], data["avg"], data["grade"]))
    print("==============================================")

if __name__ == "__main__":
    lst = []
    checkScore(lst)
    showScore(lst)



