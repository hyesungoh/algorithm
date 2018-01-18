# 이름 : 오혜성
# 날짜 : 01 18 2018
# 주제 : 연속합 중 제일 큰 것 - 1912

# DP

# 첫번째 풀이
# n = int(input())
# l = list(map(int, input().split()))
# m = l[0]
# for i in range(1, n):
#     if l[i-1] > 0 and l[i] + l[i-1] > 0:
#         l[i] += l[i-1]
#     m = l[i] if m < l[i] else m
# print(m)


input(); l = list(map(int, input().split()))
c = 0; m = l[0]
for i in l:
    if c < 0: c = 0
    c = c + i
    if m < c: m = c
print(m)