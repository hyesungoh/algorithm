# 이름 : 오혜성
# 날짜 : 01 12 2018
# 주제 : 나무 자르기 - 2805

_, n = input().split(); n=int(n)
l = list(map(int, input().split()))
low = 0; high = max(l); m = 0
while low <= high:
    mid = (low + high) // 2
    k = 0
    for i in l:
        k += i - mid if i - mid > 0 else 0
    if k >= n:
        low = mid + 1
        if m < mid: m = mid
    else:
        high = mid - 1
print(m)