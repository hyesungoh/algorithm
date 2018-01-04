# 이름 : 오혜성
# 날짜 : 01 04 2018
# 주제 : 내림차 정렬

# print(''.join(reversed(sorted(list(input())))))

# [print(i, end="") for i in reversed(sorted(input()))]

print(*sorted(input())[::-1], sep="")