# 이름 : 오혜성
# 날짜 : 04 28 2018
# 주제 : readline()을 사용한 A+B

import sys
for _ in range(int(input())):
    print(sum(map(int, sys.stdin.readline().split())))