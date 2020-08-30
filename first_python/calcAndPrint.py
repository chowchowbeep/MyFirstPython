# # list
# list_rec = list([])
# list_rec.append(input("제품코드 입력 =>"))
# list_rec.append(input("제품명 입력 =>"))
#
# list_rec.append(int(input("수량 =>")))
# list_rec.append(int(input("단가 =>")))
#
#
# list_rec.append(list_rec[2] * list_rec[3])
#
# print("\n제품코드   제품명     수량     단가    금액")
# print("==============================")
# print("%4s %3s %3d %3d %10d" %
#       (list_rec[0], list_rec[1], list_rec[2], list_rec[3], list_rec[4]) )
#
# print(list_rec)





#dict
dict_rec = {}
dict_rec["code"] = input("제품코드 입력=>")
dict_rec["product"] = input("제품명 입력=>")
dict_rec["quantity"] = int(input("수량 입력=>"))
dict_rec["wonEach"] = int(input("단가 입력=>"))


dict_rec["won"] = dict_rec["quantity"] + dict_rec["wonEach"]

#
print("%10s %10s %10s %10s %10s " % ("\n제품코드", "제품명", "수량", "단가", "금액"))
print("==============================")
print("%10s %10s %10d %10d %10d" %
      ( dict_rec["code"], dict_rec["product"], dict_rec["quantity"],
      dict_rec["wonEach"], dict_rec["won"] ))
print(dict_rec)
