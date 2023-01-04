"""
날짜 : 2023/01/04
이름 : 이해빈
내용 : 백준 3단계 더하기 사이클
"""

N = int(input())
a = N
count = 0

while True:

    b = a // 10 + a % 10
    a = a % 10 * 10 + b % 10
    count += 1

    if a == N:
        break

print(count)