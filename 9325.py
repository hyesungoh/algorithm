# 이름 : 오혜성
# 날짜 : 05 17 2018
# 주제 : 얼마? (사칙연산)

for _ in range(int(input())):
    n = int(input())
    for _ in range(int(input())):
        l = list(map(int, input().split()))
        n += l[0] * l[1]
    print(n)