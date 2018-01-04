# 이름 : 오혜성
# 날짜 : 01 04 2018
# 주제 : Counting Sort

import sys
l = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    l[int(sys.stdin.readline())] += 1
for i, n in enumerate(l):
    if n != 0:
        print((str(i)+"\n") * n, end="")