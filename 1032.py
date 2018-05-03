# 이름 : 오혜성
# 날짜 : 05 03 2018
# 주제 : 명령 프롬프트

l = []
n = int(input())
for _ in range(n):
    l.append(list(input()))

ans = l[0]
word_length = len(ans)

if n == 1: print(''.join(ans))
else:
    for i in range(1, n):
        for j in range(word_length):
            if ans[j] != l[i][j]:
                ans[j] = '?'
    print(''.join(ans))