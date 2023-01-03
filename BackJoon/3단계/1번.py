"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 3단계 구구단
"""

N = int(input())
i = 1

while i <= 9:
    print('%d * %d = %d' % (N, i, N*i))
    i += 1
