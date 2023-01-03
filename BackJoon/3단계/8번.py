"""
날짜 : 2023/01/03
이름 : 이해빈
내용 : 백준 3단계 별 찍기 - 1
"""

N = int(input())

# 첫번째 방법
for i in range(1,N+1):
    print('*'*i)


# 두번째 방법
for i in range(1, N+1):
    for k in range (1, i+1):
        print('*', end='')
    print()
