# 이름 : 오혜성
# 날짜 : 04 28 2018
# 주제 : 비내림차 정렬

import sys
l = []
for _ in range(int(input())):
    l.append(int(sys.stdin.readline()))
[print(ans) for ans in sorted(l)]

