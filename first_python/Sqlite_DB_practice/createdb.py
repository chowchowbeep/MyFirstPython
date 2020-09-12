# http://www.sqlite.org/index.html
# DB browser http://sqlitebrowser.org

import sqlite3
# 별도로 sqlite3 모듈을 설치할 필요는 없음!

dbconn = sqlite3.connect('tel.db') # 있으면 연결, 없으면 해당 이름으로 파일 생성하여 연결

dbcursor = dbconn.cursor() # sql구문 실행가능한 cursor객체를 반환
dbcursor.execute(
                "create table if not exists tel \
                    (id integer primary key autoincrement, \
                     name text, tel text, \
                     addr text, input_time text, memo text)"
                 ) # sql구문을 실행 # if not exists tel -> tel이라는 table이 존재하지 않으면 테이블을 생성
# 백슬래시 \는 연결기호

dbcursor.close()
dbconn.close()

