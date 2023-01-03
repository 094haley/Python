"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 3단계 A + B - 5
"""


while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break
    
    print(A+B)

