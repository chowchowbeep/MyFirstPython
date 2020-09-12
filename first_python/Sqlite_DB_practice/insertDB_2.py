import sqlite3
import time

dbconn = sqlite3.connect('tel.db')

dbcursor = dbconn.cursor()

data = [
    ('홍기자', '010-1111-1111', '서울', str(time.asctime(time.localtime(time.time()))), '테스트1'),
    ('한기자', '010-1111-1112', '대전', str(time.asctime(time.localtime(time.time()))), '테스트1'),
    ('김기자', '010-1111-1113', '부산', str(time.asctime(time.localtime(time.time()))), '테스트1')
]

sql = "insert into tel (name, tel, addr, input_time, memo) \
    values (?, ?, ?, ?, ?)"
dbcursor.executemany(sql, data) # data가 리스트 형태(파라미터가 다수)인 경우 반복해서 sql을 처리하는 경우

dbconn.commit()

for row in dbcursor.execute("select * from tel"):
    print(row)

dbcursor.close()

dbconn.close()