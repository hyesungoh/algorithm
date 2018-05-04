# 이름 : 오혜성
# 날짜 : 05 04 2018
# 주제 : 일곱 난쟁이

l = []
for _ in range(9):
    l.append(int(input()))
ans = sum(l)
ischeck = False

for i in range(9):
    for j in range(i+1, 9):
        if ans - (l[i] + l[j]) == 100:
            l.pop(i)
            if i > j:
                l.pop(j)
            else:
                l.pop(j-1)
            ischeck = True
            break

    if ischeck == True:
        break

[print(i) for i in sorted(l)]