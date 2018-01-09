# 이름 : 오혜성
# 날짜 : 01 09 2018
# 주제 : 1002번 문제, 두 원의 교점

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2; m = (r1 - r2) ** 2; p = (r1 + r2) ** 2
    if d == 0 and r1 == r2: print(-1)
    elif d < m or d > p: print(0)
    elif m < d < p: print(2)
    else: print(1)