"""
날짜 : 2023/01/02
이름 : 이해빈
내용 : 백준 1단계 곱셈
"""

a = int(input())
b = int(input())


print(a * (b % 10))
print(a * (b % 100 //10))
print(a * (b // 100))
print(a * b)
