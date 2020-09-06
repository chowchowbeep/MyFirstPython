import csv


#f = open('data.csv', 'r', encoding='utf-8', newline='')
f = open('output.csv', 'r', encoding='utf-8', newline='')

# reader()메소드는 파일을 행단위로 읽어서 list타입 객체로 반환
#rdr = csv.reader(f)

# delimiter는 기본값이 , 이지만 다른 문자를 구분자로 하여 파일을 읽어들일 수도 있음
# (구분자를 ,가 아닌 다른 문자로 하여 write한 경우, read할 때 구분자 지정을 동일하게 해 주어야 함)
rdr = csv.reader(f, delimiter=" ")

print(rdr)

for line in rdr:
    print(line)
    for item in line:
      print(item)
    print()

f.close()



'''
['1', '김초엽', '2020-09-06 11:20:23', '31']
1
김초엽
2020-09-06 11:20:23
31
'''