"""
날짜 : 2023/01/13
이름 : 이해빈
내용 : 파이썬 사용자 관리 프로그램 실습
"""
import pymysql
from sub.User3VO import User3VO


# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234', 
                        db='java2db', 
                        charset='utf8')

cur = conn.cursor()

while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0

    try:
        answer = int(input('선택 :',))
    except:
        print('숫자를 입력하세요.')
        continue

    if answer == 0:
        break
    elif answer == 1:
    
        user = list(input('아이디, 이름, 휴대폰, 나이 순으로 입력: ').split())

        sql = "insert into `user3` values('%s', '%s', '%s', '%s')" % (user[0], user[1], user[2], user[3])

        cur.execute(sql)
        conn.commit()
        print('등록완료...')

    elif answer == 2:
                
        cur.execute("select * from `user3`")
        conn.commit()

        for row in cur.fetchall():
            print('-------------------------------')
            print('|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3]))


        print('조회완료...')

    elif answer == 3:
        
        name = input('이름을 입력하세요: ')

        sql = "select * from `user3` where `name`='%s'" % name
        cur.execute(sql)
        conn.commit()

        row = cur.fetchone()
        
        print('-----------------')
        print('|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3]))

        print('검색완료...')

    elif answer == 4:
        name = input('삭제할 이름을 입력하세요: ')

        sql = "delete from `user3` where `name`='%s'" % name
        cur.execute(sql)
        conn.commit()

        print('삭제완료...')
        
    else:
        print('0 ~ 4 중에서 입력하세요.')

# 데이터베이스 종료
conn.close()
print('프로그램 종료...')