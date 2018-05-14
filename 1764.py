# 이름 : 오혜성
# 날짜 : 05 15 2018
# 주제 : 문자열 중복 확인

n1, n2 = input().split()

l1 = []
l2 = []

for _ in range(int(n1)):
    l1.append(input())
for _ in range(int(n2)):
    l2.append(input())

ans_list = sorted(list(set(l1) & set(l2)))

print(len(ans_list))
[print(i) for i in ans_list]