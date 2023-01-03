"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 2단계 알람 시계
"""

H, M = map(int, input().split())

if M >= 45 :
    M -= 45
else :
    if H == 0 :
        H = 23
        M += 15
    else :
        H -= 1
        M += 15

print(H, M)