# 이름 : 오혜성
# 날짜 : 05 11 2018
# 주제 : 나이 순으로 정렬

l = []
for _ in range(int(input())):
    l.append(input().split())

sorted_list = sorted(l, key=lambda p: int(p[0]))
[print(i[0], i[1]) for i in sorted_list]