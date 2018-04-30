# 이름 : 오혜성
# 날짜 : 04 30 2018
# 주제 : 하얀 칸

n = 0
for t in range(8):
    s = list(input())
    if t%2 == 0:
        for i in range(8):
            if i%2 == 0 and s[i] == 'F':
                n += 1
    else:
        for i in range(8):
            if i%2 == 1 and s[i] == 'F':
                n += 1

print(n)