"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 3단계 별 찍기 - 2
"""

N = int(input())

for i in range(1, N+1):
    print(' ' * (N-i) + '*' * i)