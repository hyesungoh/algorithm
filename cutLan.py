# 이름 : 오혜성
# 날짜 : 01 12 2018
# 주제 : n개의 랜선을 k개의 랜선으로 만들 때 최대 길이 - 1654

# readline으로 시간 감소
# import sys
# x, n = sys.stdin.readline().split()
# x, n = int(x), int(n)
# l = []; m = 0
# for _ in range(x):
#     l.append(int(sys.stdin.readline()))
# low = 0; high = max(l)
# while low <= high:
#     mid = (high + low + 1) // 2
#     ans = 0
#     for j in l: ans += (j // mid)
#     if ans >= n:
#         low = mid + 1
#         if mid > m: m = mid
#     else: high = mid - 1
# print(m)


# 숏코딩
x, n = map(int, input().split())
l = []; m = 0
[l.append(int(input())) for _ in range(x)]
low = 0; high = max(l)
while low <= high:
    mid = (high + low + 1) // 2
    ans = 0
    for j in l: ans += (j // mid)
    if ans >= n:
        low = mid + 1
        if mid > m: m = mid
    else: high = mid - 1
print(m)