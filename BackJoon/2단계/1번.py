"""
날짜 : 2023/01/02
이름 : 이해빈
내용 : 백준 2단계 두 수 비교하기
"""

a, b = map(int, input().split())

if(a > b) : 
    print('>')
elif(a < b) :
    print('<')
elif(a == b) :
    print('==')
