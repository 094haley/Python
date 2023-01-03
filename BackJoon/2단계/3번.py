"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 2단계 윤년
"""


num = int(input())

if num % 4 == 0 and num % 100 != 0 :
    print(1)
elif num % 400 == 0 :
    print(1)
else : 
    print(0)