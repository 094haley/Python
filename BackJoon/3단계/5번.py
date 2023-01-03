"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 3단계 빠른 A + B
"""

import sys

T = int(input())

for i in range (1,T+1):
    A, B = map(int,sys.stdin.readline().split())
    print(A+B)
