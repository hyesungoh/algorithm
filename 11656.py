# 이름 : 오혜성
# 날짜 : 04 28 2018
# 주제 : 접미사 배열, 사전 순 정렬

w = input()
lw = len(w)

l = list(map(lambda x: w[x:lw], range(lw)))
[print(ans) for ans in sorted(l)]