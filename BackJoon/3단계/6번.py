"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 3단계 A + B - 7
"""

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #{}: {}'.format(i+1, A+B))


# 모아서 출력하기
T = int(input())
str = []
k = 1

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    str.append(A+B)

for j in str:
    print('Case #{}: {}'.format(k, i))
    k+=1

