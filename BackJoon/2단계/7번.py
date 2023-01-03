"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 2단계 주사위 세개
"""


a, b, c = map(int, input().split())

m = 0

if a == b and b == c :
    m = 10000 + a * 1000 
elif a == b or b == c or c == a:
    if a == b or b == c:
        m = 1000 + b * 100
    elif c == a:
        m = 1000 + c * 100
else:
    if a > b and a > c:
        m= a * 100
    elif b > a and b > c:
        m= b * 100
    elif c > b and c > a:
        m= c * 100

print(m)
