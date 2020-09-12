import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()


name=input("수정할 이름 입력 : ")
res = dbcursor.execute('SELECT * FROM TEL WHERE NAME = ?', (name,))
# (name,)튜플형식의 데이터로 인식시키기 위해 콤마, 붙임

flag = 0
for row in res:
    tel = input("전화번호 : ")
    addr = input("주소 : ")
    memo = input("메모 : ")
    dbcursor.execute("update tel set tel=?, addr=?, memo=? where name=?",
                     (tel, addr, memo, name))
    dbconn.commit()
    flag = 1

if flag == 0:
    print("\n 수정실패! \n")
else:
    print("\n 수정성공! \n")

dbcursor.close()
dbconn.close()