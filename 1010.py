# 이름 : 오혜성
# 날짜 : 05 30 2018
# 주제 : 다리 놓기, 조합

from math import factorial as f

for case in range(int(input())):
    n, m = map(int, input().split())
    noc = int(f(m) / (f(n) * f(m - n)))
    print(noc)
