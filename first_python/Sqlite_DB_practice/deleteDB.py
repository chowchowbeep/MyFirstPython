import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res = dbcursor.execute('SELECT * FROM TEL ORDER BY ID DESC')


name = input("삭제할 이름 입력 : ")
flag = 0
for row in res:
    if row[1] == name:
        dbcursor.execute("delete from tel where name=?", (name,))
        dbconn.commit()
        flag = 1
        break

if flag == 0:
    print("\n 삭제실패! \n")
else:
    print("\n 삭제성공! \n")

dbcursor.close()
dbconn.close()