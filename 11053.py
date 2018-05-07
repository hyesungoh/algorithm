# 이름 : 오혜성
# 날짜 : 05 07 2018
# 주제 : 가장 긴 증가하는 부분 수열

length = int(input())
l = list(map(int, input().split(" ")))
dp = [0] * (length + 2)
for i in range(0, length):
    dp[i] = 1
    for j in range(0, i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# for i in range(length-1, -1, -1):
#     s = set(l[0:i+1])
#     dp.append(len(list(filter(lambda x: x <= l[i], s))))
# print(max(dp))

# for i in range(length):
#     temp = 0
#     temp_add = 0
#     for j in range(i, length):
#         if temp < l[j]:
#             temp_add += 1
#             temp = l[j]
#     ans.append(temp_add)
#
# print(ans)
# print(max(ans))