import csv

# csv 파일 생성 및 쓰기
# 데이터분석시 csv파일 주로 사용

f = open('output.csv', 'w', encoding='utf-8', newline='')

# 구분자delimiter 기본값은 ,콤마
# quote는 데이터의 단위를 만들어줌.
# (구분자가 데이터에 포함되어 있어도 적절하게 데이터를 구분하여 출력할 수 있게 해 줌)
#wr = csv.writer(f, delimiter="/", quotechar='"', quoting=csv.QUOTE_ALL)
wr = csv.writer(f, delimiter=" ")


# 쓰기할 때는 주로 튜플, 리스트 구조를 사용
wr.writerow((1, "김초롱", True))
wr.writerow([2, "김누구", False])

f.close()