"""
날짜 : 2023/01/02
이름 : 이해빈
내용 : 백준 1단계 나머지
"""

a, b, c = map(int, input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
