"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 2단계 오븐 시계
"""

A, B = map(int, input().split())
C = int(input())

if B + C >= 60 :
    A += (B + C) // 60
    B = (B + C) % 60
    if A >= 24 :
        A -= 24
else :
    B += C

print(A, B)