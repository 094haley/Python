"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 3단계 영수증
"""

X = int(input())
N = int(input())

total = 0

for i in range(1, N+1):
    a, b = map(int, input().split())
    total += a * b

if X == total :
    print('Yes')
else:
    print('No')