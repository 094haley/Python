"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 3단계 A + B - 8
"""

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(i+1, A, B, A+B))
