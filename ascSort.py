# 이름 : 오혜성
# 날짜 : 01 04 2018
# 주제 : 오름차 정렬

# list sort 사용시 속도 이슈로 인해 numpy 사용해보았지만 BOJ에서 런타임 에러 발생
# import numpy as np
# l = [0] * int(input())
# for i in range(len(l)):
#     l[i] = int(input())
# [print(i) for i in np.msort(np.array(l))]

import sys
r = lambda: int(sys.stdin.readline()); l = []
[l.append(r()) for _ in range(r())]
print(*sorted(l), sep="\n")