import sqlite3


dbconn = sqlite3.connect('sungjuk.db')
dbcursur = dbconn.cursor()

dbcursur.execute("create table sungjuk ( \
    hakbum test primary kery not null, \
    irum text, kor integer, eng integer, math integer )"
)

# 조회할 학번을 입력하세요

