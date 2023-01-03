"""
날짜 : 2023/01/02
이름 : 이해빈
내용 : 백준 2단계 시험 성적
"""

score = int(input()) 

if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else :
    print('F')